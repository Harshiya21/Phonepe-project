import git
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 
import mysql.connector
import matplotlib.pyplot as plt 
import plotly.express as px 
import requests 
import json 
import os

# repository_url = "https://github.com/PhonePe/pulse.git"
# destination_directory =r"C:\Users\nawas\Desktop\PHONE_PAY\data"
# git.Repo.clone_from(repository_url, destination_directory)

#Agg_Trans

#This is to direct the path to get the data as states

path="c:/Users/nawas/Desktop/PHONE_PAY/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)

clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
    for k in Agg_yr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        A=json.load(Data)
        for z in A['data']['transactionData']:
            Name=z['name']
            count=z['paymentInstruments'][0]['count']
            amount=z['paymentInstruments'][0]['amount']
            clm['Transaction_type'].append(Name)
            clm['Transaction_count'].append(count)
            clm['Transaction_amount'].append(amount)
            clm['State'].append(i)
            clm['Year'].append(j)
            clm['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Agg_Trans_df=pd.DataFrame(clm)
Agg_Trans_df['State']= Agg_Trans_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Trans_df['State']= Agg_Trans_df['State'].str.replace("-"," ")
Agg_Trans_df['State']= Agg_Trans_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Agg_Trans_df['State']= Agg_Trans_df['State'].str.title()
#print(Agg_Trans_df)

#AGG Users
#This is to direct the path to get the data as states

path1="c:/Users/nawas/Desktop/PHONE_PAY/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path1)

clm1={'State':[], 'Year':[],'Quater':[],'Brand':[],'Transaction_count':[],'Percentage':[]}

for i in Agg_state_list:
    p_i=path1+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            B=json.load(Data)
        try:
            for z in B['data']['usersByDevice']:
                Brand=z['brand']
                count=z['count']
                Percentage=z['percentage']
                clm1['Brand'].append(Brand)
                clm1['Transaction_count'].append(count)
                clm1['Percentage'].append(Percentage)
                clm1['State'].append(i)
                clm1['Year'].append(j)
                clm1['Quater'].append(int(k.strip('.json')))
        except:
            pass

#Succesfully created a dataframe
Agg_Users_df=pd.DataFrame(clm1)
Agg_Users_df['State']= Agg_Users_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Users_df['State']= Agg_Users_df['State'].str.replace("-"," ")
Agg_Users_df['State']= Agg_Users_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Agg_Users_df['State']= Agg_Users_df['State'].str.title()
#print(Agg_Users_df)

#MAP trans

path2="c:/Users/nawas/Desktop/PHONE_PAY/data/map/transaction/hover/country/india/state/"
Map_state_list=os.listdir(path2)

clm2={'State':[], 'Year':[],'Quater':[],'District':[],'Transaction_count':[],'Transaction_amount':[]}

for i in Map_state_list:
    p_i=path2+i+"/"
    Map_yr=os.listdir(p_i)
    for j in Map_yr:
        p_j=p_i+j+"/"
        Map_yr_list=os.listdir(p_j)
        for k in Map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            C=json.load(Data)
            for z in C['data']['hoverDataList']:
                Name=z['name']
                count=z['metric'][0]['count']
                amount=z['metric'][0]['amount']
                clm2['District'].append(Name)
                clm2['Transaction_count'].append(count)
                clm2['Transaction_amount'].append(amount)
                clm2['State'].append(i)
                clm2['Year'].append(j)
                clm2['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Map_Trans_df=pd.DataFrame(clm2)
Map_Trans_df['State']= Map_Trans_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_Trans_df['State']= Map_Trans_df['State'].str.replace("-"," ")
Map_Trans_df['State']= Map_Trans_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Map_Trans_df['State']= Map_Trans_df['State'].str.title()
#print(Map_Trans_df)

#MAP USERS
path3="c:/Users/nawas/Desktop/PHONE_PAY/data/map/user/hover/country/india/state/"
Map_state_list=os.listdir(path3)

clm3={'State':[], 'Year':[],'Quater':[],'Districts':[],'RegisteredUsers':[],'AppOpens':[]}

for i in Map_state_list:
    p_i=path3+i+"/"
    Map_yr=os.listdir(p_i)
    for j in Map_yr:
        p_j=p_i+j+"/"
        Map_yr_list=os.listdir(p_j)
        for k in Map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
        for z in D['data']['hoverData'].items():
            District=z[0]
            registeredUsers=z[1]['registeredUsers']
            appOpens=z[1]['appOpens']
            clm3['Districts'].append(District)
            clm3['RegisteredUsers'].append(registeredUsers)
            clm3['AppOpens'].append(appOpens)
            clm3['State'].append(i)
            clm3['Year'].append(j)
            clm3['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Map_Users_df=pd.DataFrame(clm3)
Map_Users_df['State']= Map_Users_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Map_Users_df['State']= Map_Users_df['State'].str.replace("-"," ")
Map_Users_df['State']= Map_Users_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Map_Users_df['State']= Map_Users_df['State'].str.title()
#print(Map_Users_df)

#TOP_Trans

path4="c:/Users/nawas/Desktop/PHONE_PAY/data/top/transaction/country/india/state/"
Top_state_list=os.listdir(path4)

clm4={'State':[], 'Year':[],'Quater':[],'Pincodes':[],'Transaction_count':[],'Transaction_amount':[]}

for i in Top_state_list:
    p_i=path4+i+"/"
    Top_yr=os.listdir(p_i)
    for j in Top_yr:
        p_j=p_i+j+"/"
        Top_yr_list=os.listdir(p_j)
        for k in Top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            E=json.load(Data)
        for z in E['data']['pincodes']:
            entityName=z['entityName']
            count=z['metric']['count']
            amount=z['metric']['amount']
            clm4['Pincodes'].append(entityName)
            clm4['Transaction_count'].append(count)
            clm4['Transaction_amount'].append(amount)
            clm4['State'].append(i)
            clm4['Year'].append(j)
            clm4['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_Trans_df=pd.DataFrame(clm4)
Top_Trans_df['State']= Top_Trans_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_Trans_df['State']= Top_Trans_df['State'].str.replace("-"," ")
Top_Trans_df['State']= Top_Trans_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Top_Trans_df['State']= Top_Trans_df['State'].str.title()
#print(Top_Trans_df)

#Top_Users

path5="c:/Users/nawas/Desktop/PHONE_PAY/data/top/user/country/india/state/"
Top_state_list=os.listdir(path5)

clm5={'State':[], 'Year':[],'Quater':[],'Pincodes':[],'RegisteredUsers':[]}

for i in Top_state_list:
    p_i=path5+i+"/"
    Top_yr=os.listdir(p_i)
    for j in Top_yr:
        p_j=p_i+j+"/"
        Top_yr_list=os.listdir(p_j)
        for k in Top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
        for z in F['data']['pincodes']:
            Name=z['name']
            registeredUsers=z['registeredUsers']
            clm5['Pincodes'].append(Name)
            clm5['RegisteredUsers'].append(registeredUsers)
            clm5['State'].append(i)
            clm5['Year'].append(j)
            clm5['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Top_Users_df=pd.DataFrame(clm5)
Top_Users_df['State']= Top_Users_df['State'].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_Users_df['State']= Top_Users_df['State'].str.replace("-"," ")
Top_Users_df['State']= Top_Users_df['State'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra & Nagar Haveli & Daman & Diu ")
Top_Users_df['State']= Top_Users_df['State'].str.title()
#print(Top_Users_df)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="phonepae")
print(mydb)
mycursor = mydb.cursor(buffered=True)

# mycursor.execute('create database phonepae')
# mycursor.execute("use phonepae")

#Agg Trans
#Agg_Trans table creation
Agg_Trans_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Agg_Trans(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                Transaction_type VARCHAR(255),
                                                                Transaction_count INT,
                                                                Transaction_amount INT)''')
mydb.commit()
#Agg_Trans inserting process
Agg_Trans_insert='''INSERT INTO phonepae.Agg_Trans(State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
VALUES(%s, %s, %s, %s, %s, %s) '''
data=Agg_Trans_df.values.tolist()
mycursor.executemany(Agg_Trans_insert,data)
mydb.commit()

#Agg Users
#Agg_Users table creation
Agg_Users_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Agg_Users(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                Brand VARCHAR(255),
                                                                Transaction_count INT,
                                                                Percentage FLOAT)''')
mydb.commit()
#Agg_Users inserting process
Agg_Users_insert='''INSERT INTO phonepae.Agg_Users(State, Year, Quarter, Brand, Transaction_count, Percentage)
VALUES(%s, %s, %s, %s, %s, %s) '''
data=Agg_Users_df.values.tolist()
mycursor.executemany(Agg_Users_insert,data)
mydb.commit()

#Map Trans
#Map_Trans table creation
Map_Trans_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Map_Trans(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                District VARCHAR(255),
                                                                Transaction_count INT,
                                                                Transaction_amount INT)''')
mydb.commit()

#Map_Trans inserting process
Map_Trans_insert='''INSERT INTO phonepae.Map_Trans(State, Year, Quarter, District, Transaction_count, Transaction_amount)
VALUES(%s, %s, %s, %s, %s, %s) '''
data=Map_Trans_df.values.tolist()
mycursor.executemany(Map_Trans_insert,data)
mydb.commit()

#Map Users
#Map_Users table creation
Map_Users_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Map_Users(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                Districts VARCHAR(255),
                                                                RegisteredUsers INT,
                                                                AppOpens INT)''')
mydb.commit()
#Map_Users inserting process
Map_Users_insert='''INSERT INTO phonepae.Map_Users(State, Year, Quarter, Districts, RegisteredUsers, AppOpens)
VALUES(%s, %s, %s, %s, %s, %s) '''
data=Map_Users_df.values.tolist()
mycursor.executemany(Map_Users_insert,data)
mydb.commit()

#Top Trans
#Top_Trans table creation
Top_trans_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Top_trans(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                Pincodes INT,
                                                                Transaction_count INT,
                                                                Transaction_amount INT)''')
mydb.commit()
#Top_trans inserting process
Top_trans_insert='''INSERT INTO phonepae.Top_trans(State, Year, Quarter, Pincodes, Transaction_count, Transaction_amount)
VALUES(%s, %s, %s, %s, %s, %s) '''
data=Top_Trans_df.values.tolist()
mycursor.executemany(Top_trans_insert,data)
mydb.commit()

#TOP Users
#Top_Users table creation
Top_Users_table=mycursor.execute('''CREATE TABLE IF NOT EXISTS phonepae.Top_Users(State VARCHAR(255),
                                                                Year INT,
                                                                Quarter INT,
                                                                Pincodes INT,
                                                                RegisteredUsers INT)''')
mydb.commit()
#Top_Users inserting process
Top_Users_insert='''INSERT INTO phonepae.Top_Users(State, Year, Quarter, Pincodes, RegisteredUsers)
VALUES(%s, %s, %s, %s, %s) '''
data=Top_Users_df.values.tolist()
mycursor.executemany(Top_Users_insert,data)
mydb.commit()

#streamlit part 

st.set_page_config(
    page_title="Phonep Pulse",
    page_icon="c:/Users/nawas/Downloads/phonepe image.png",
    layout="wide")

with st.sidebar:
    select_options = option_menu("Main Menu", ["Home","Data Explore", "INSIGHTS", "GEO VISUALIZATION"])
    
if select_options == "Home":

    st.title(':violet[PHONEPE PULSE DATA VISUALIZATION AND EXPLORATION]')

    col1,col2 = st.columns(2)

    with col1:
        st.header(":violet[PHONEPE]")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.write("****FEATURES****")
        st.write("****✳Credit & Debit card linking****")
        st.write("****✳Bank Balance check****")
        st.write("****✳Money Storage****")
        st.write("****✳PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/about-us/")

    with col2:
        video_file1 = open(r"c:\Users\nawas\Downloads\pulse-video.mp4",'rb')
        video_bytes = video_file1.read()

        st.video(video_bytes)

if select_options == "Data Explore":
    
    selected_trans_user = st.selectbox("Select Type",["Transactions","Users"])
    
    years = list(range(2018,2024))
    selected_year = st.selectbox("Select year",years)
    quarters = ["Q1 (Jan - Mar)", "Q2 (Apr - Jun)", "Q3 (Jul - Sep)", "Q4 (Oct - Dec)"]
    selected_quarter = st.selectbox("Select Quarter", quarters)

    #TOP 10 states 
    if(selected_trans_user == 'Transactions'):
            # Add custom CSS to control the column spacing
        col1,col2,col3 =st.columns([2,2,2])
        with col1:
            st.markdown("### :violet[States]")
            query1 =f""" SELECT State,SUM(Transaction_amount) AS Transaction_Amount,SUM(Transaction_count) AS Transaction_Count From Agg_Trans WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY State ORDER BY Transaction_Amount DESC LIMIT 10"""
                    
            mycursor.execute(query1)

            df_1=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Amount","Transaction_Count"])

            fig_pie_1 = px.pie(df_1, names="State", values="Transaction_Amount",
                                hover_data="Transaction_Count",title='Top 10 States',color_discrete_sequence=px.colors.sequential.Agsunset)           

            fig_pie_1.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie_1,use_container_width=True)
            
            #TOP 10 District  
        with col2:
            st.markdown("### :violet[Districts]")    
            query2 =f""" SELECT District,SUM(Transaction_amount) AS Transaction_Amount,SUM(Transaction_count) AS Transaction_Count From Map_Trans WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY District ORDER BY Transaction_Amount DESC LIMIT 10"""
                    
            mycursor.execute(query2)

            df_2=pd.DataFrame(mycursor.fetchall(),columns=["District","Transaction_Amount","Transaction_Count"])

            fig_pie_2 = px.pie(df_2, names="District", values="Transaction_Amount",
                                hover_data="Transaction_Count",title='Top 10 Districts',color_discrete_sequence=px.colors.sequential.Agsunset_r)           

            fig_pie_2.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie_2,use_container_width=True)
                    
            #TOP 10 Pincodes 
        with col3:
            st.markdown("### :violet[Pincodes]")
            query3 =f""" SELECT Pincodes,SUM(Transaction_amount) AS Transaction_Amount,SUM(Transaction_count) AS Transaction_Count From Top_trans WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY Pincodes ORDER BY Transaction_Amount DESC LIMIT 10"""
                    
            mycursor.execute(query3)

            df_3=pd.DataFrame(mycursor.fetchall(),columns=["Pincodes","Transaction_Amount","Transaction_Count"])

            fig_pie_3 = px.pie(df_3, names="Pincodes", values="Transaction_Amount",
                                hover_data="Transaction_Count",title='Top 10 Pincodes',color_discrete_sequence=px.colors.sequential.Rainbow)           

            fig_pie_3.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie_3,use_container_width=True)
        
    if(selected_trans_user == 'Users'):
        col1,col2,col3 =st.columns([2,2,2])
        #TOP 10 State
        with col1:
            st.markdown("### :violet[States]")
            query_1 =f""" SELECT State,SUM(RegisteredUsers) AS RegisteredUsers, SUM(AppOpens) AS AppOpens From Map_Users WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY State ORDER BY RegisteredUsers DESC LIMIT 10"""
                    
            mycursor.execute(query_1)

            User_df_1=pd.DataFrame(mycursor.fetchall(),columns=["State","RegisteredUsers","AppOpens"])

            fig_pie_1 = px.pie(User_df_1, names="State", values="RegisteredUsers",
                                hover_data="AppOpens",title='Top 10 States',color_discrete_sequence=px.colors.sequential.Agsunset)           

            fig_pie_1.update_traces(textposition='inside', textinfo='percent+label')

            st.plotly_chart(fig_pie_1,use_container_width=True)
                
        #TOP 10 District  
        with col2:
            st.markdown("### :violet[Districts]")
            query_2 =f""" SELECT Districts,SUM(RegisteredUsers) AS RegisteredUsers,SUM(AppOpens) AS AppOpens From Map_Users WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY Districts ORDER BY RegisteredUsers DESC LIMIT 10"""
                    
            mycursor.execute(query_2)

            User_df_2=pd.DataFrame(mycursor.fetchall(),columns=["Districts","RegisteredUsers","AppOpens"])

            fig_pie_2 = px.pie(User_df_2, names="Districts", values="RegisteredUsers",
                                hover_data="AppOpens",title='Top 10 District',color_discrete_sequence=px.colors.sequential.Agsunset_r)           

            fig_pie_2.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie_2,use_container_width=True)

        #TOP 10 Pincodes 
        with col3:
            st.markdown("### :violet[Pincodes]")
            query_3 =f""" SELECT State,Pincodes,SUM(RegisteredUsers) AS RegisteredUsers From Top_Users WHERE year =  {selected_year} AND quarter = {quarters.index(selected_quarter)+1} GROUP BY Pincodes ORDER BY RegisteredUsers DESC LIMIT 10"""
                    
            mycursor.execute(query_3)

            User_df_3=pd.DataFrame(mycursor.fetchall(),columns=["State","Pincodes","RegisteredUsers"])

            fig_pie_3 = px.pie(User_df_3, names="Pincodes", values="RegisteredUsers",
                                    hover_data="State",title='Top 10 Pincodes',color_discrete_sequence=px.colors.sequential.Rainbow)           

            fig_pie_3.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie_3,use_container_width=True) 

if select_options == "INSIGHTS":
    
    questions= st.selectbox("Select all questions",("1.Top 10 States Amount Transactions",
                                                "2.Least 10 Districts based on the Transaction Amount",
                                                "3.Least 10 Pincodes along with States Total Transactions",
                                                "4.Least 10 Mobile Brands based on the Transaction Count",
                                                "5.States based on Transaction Count",
                                                "6.States based on Total Transactions",
                                                "7.Least 10 States Total Phonepe Users and App opens in INDIA ",
                                                "8.List out the district in tamilnadu who had Open and Using phonepe",
                                                "9.Least 10 Pincodes along with States Total Phonepe Users",
                                                "10.List the Payments and Types of Transactions conducted in each Union Territory using PhonePe"))
    
    if questions == "1.Top 10 States Amount Transactions":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State,Transaction_amount AS Transaction_Amount \
        FROM Agg_Trans \
        GROUP BY State \
        ORDER BY Transaction_Amount DESC \
        LIMIT 10''')
        df1=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Amount"])
        st.write(df1)
        fig_bar_1=px.bar(df1,x="State",y="Transaction_Amount",title="Top 10 States Amount Transactions",
                        width=600,color="State",color_discrete_sequence=px.colors.sequential.Rainbow)
        st.plotly_chart(fig_bar_1)
        st.subheader("Insights")
        st.write("Maharashtra has a significantly higher value compared to other states, with a notable difference from the next highest states, Karnataka and Delhi. Madhya Pradesh has the lowest value, reflecting a considerable disparity across the listed states")

    elif questions == "2.Least 10 Districts based on the Transaction Amount":    
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT District,SUM(Transaction_amount) AS Transaction_Amount \
        FROM Map_Trans \
        GROUP BY District \
        ORDER BY Transaction_Amount ASC \
        LIMIT 10''')
        df2=pd.DataFrame(mycursor.fetchall(),columns=["District","Transaction_Amount"])
        st.write(df2)
        fig_line_2 = px.line(df2, x="District", y="Transaction_Amount",title ="Least 10 Districts by Transaction Amount", width=1000, height=800,
                        markers=True, color_discrete_sequence=px.colors.sequential.Magenta)
        st.plotly_chart(fig_line_2)
        st.subheader("Insights")
        st.write("Muzaffarabad, Kamle, and Longleng districts have notably higher transaction amounts, suggesting significant economic activity. Pherzawl district shows the lowest transaction amount, indicating lesser activity compared to the others")

    elif questions == "3.Least 10 Pincodes along with States Total Transactions":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State, Pincodes, SUM(Transaction_amount) AS Transaction_Amount \
        FROM Top_trans \
        GROUP BY State,Pincodes \
        ORDER BY Transaction_Amount ASC \
        LIMIT 10''')
        df3=pd.DataFrame(mycursor.fetchall(),columns=["State","Pincodes","Transaction_Amount"])
        st.write(df3)
        fig_sunburst_3 = px.sunburst(df3, path=["State","Transaction_Amount"],values="Pincodes",
                                    title ="Total Transactions")
        st.plotly_chart(fig_sunburst_3)
        st.subheader("Insights")
        st.write("The highest transaction amount is in Tripura (799125) at 5,890,832, while the lowest is in Mizoram (796421) at 865,716. Mizoram and Meghalaya show multiple entries, indicating diverse economic activities within these states")

    elif questions == "4.Least 10 Mobile Brands based on the Transaction Count":    
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT Brand,SUM(Transaction_count) AS Transaction_Count \
        From Agg_Users \
        GROUP BY Brand \
        ORDER BY Transaction_Count ASC \
        LIMIT 10''')
        df4=pd.DataFrame(mycursor.fetchall(),columns=["Brand","Transaction_Count"])
        df4["Transaction_Count"] = df4["Transaction_Count"].astype(float)  
        st.write(df4)
        fig_bar_brand = px.bar(df4,y="Brand",x="Transaction_Count", width=1000, height=800,
                            color="Brand",color_discrete_sequence=px.colors.sequential.Cividis)
        st.plotly_chart(fig_bar_brand)
        st.subheader("Insights")
        st.write("OnePlus and Huawei lead in transaction counts, indicating high consumer engagement, with 11.7 billion and 10.6 billion transactions, respectively. HMD Global has the lowest count at 138 million, suggesting a smaller market presence compared to other brands listed")


    elif questions == "5.States based on Transaction Count":    
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State,AVG(Transaction_count) AS Transaction_Count \
        FROM Top_Trans \
        GROUP BY State \
        ORDER BY Transaction_Count DESC''')
        df5=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Count"])
        st.write(df5)
        fig_bar_5 = px.bar(df5, x="State", y="Transaction_Count",title="State by Transaction Count",
                            width=600,color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig_bar_5)
        st.subheader("Insights")
        st.write("Telangana has the highest transaction count at 32 million, indicating high economic activity. Lakshadweep has the lowest count at 2,354, suggesting minimal activity")


    elif questions == "6.States based on Total Transactions":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State,SUM(Transaction_amount) AS Transaction_Amount
        FROM Top_Trans \
        GROUP BY State \
        ORDER BY Transaction_Amount DESC''')
        df6=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Amount"])
        st.write(df6)
        fig_bar_6 = px.bar(df6, x="State", y="Transaction_Amount",title="States based on Total Transactions",
                        color="State",width=600,color_discrete_sequence=px.colors.sequential.Rainbow)
        st.plotly_chart(fig_bar_6)
        st.subheader("Insights") 
        st.write("Karnataka leads with the highest transaction amount at approximately 87 trillion, followed by Telangana and Delhi. Lakshadweep has the lowest transaction amount, indicating a stark contrast in economic activity across the regions")


    elif questions == "7.Least 10 States Total Phonepe Users and App opens in INDIA ":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State,SUM(RegisteredUsers) AS RegisteredUsers,SUM(AppOpens) AS AppOpens \
        FROM Map_Users \
        GROUP BY State \
        ORDER BY RegisteredUsers,AppOpens ASC \
        LIMIT 10''')
        df7=pd.DataFrame(mycursor.fetchall(),columns=["State","RegisteredUsers","AppOpens"])
        st.write(df7)
        fig_sunburst_7 = px.sunburst(df7, path=["State","AppOpens"], values="RegisteredUsers",
                                    title="Least 10 States Total Phonepe Users and App opens")
        st.plotly_chart(fig_sunburst_7)
        st.subheader("Insights")
        st.write("Dadra & Nagar Haveli & Daman & Diu has the highest app opens at approximately 61.9 billion, despite having fewer registered users compared to some other states. Arunachal Pradesh and Manipur also show high engagement with significant app opens relative to their user numbers")

    elif questions == "8.List out the district in tamilnadu who had Open and Using phonepe":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State, Districts, SUM(RegisteredUsers) AS RegisteredUsers \
        FROM Map_Users \
        WHERE State = "Tamil Nadu"  \
        GROUP BY Districts,State \
        ORDER BY RegisteredUsers DESC \
        LIMIT 10''')
        df8=pd.DataFrame(mycursor.fetchall(),columns=["State","Districts","RegisteredUsers"])
        st.write(df8)
        fig_bar_8=px.bar(df8, x="Districts", y="RegisteredUsers",
                        title="Top 10 Districts in Tamil Nadu ",
                        width=600,color_discrete_sequence=px.colors.sequential.Rainbow)
        
        st.plotly_chart(fig_bar_8)
        st.subheader("Insights")
        st.write ("Like many other high GDP states, Tamil Nadu also boasts a significant user base across all its districts, with transactions steadily increasing over the past few years. With its robust infrastructure, sustained economic growth, high GDP, and dense population, Tamil Nadu ranks among the top 10 states in PhonePe data ")

    elif questions == "9.Least 10 Pincodes along with States Total Phonepe Users": 
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State, Pincodes, SUM(RegisteredUsers) AS RegisteredUsers \
        FROM Top_Users\
        GROUP BY State,Pincodes \
        ORDER BY RegisteredUsers ASC \
        LIMIT 10''')
        df9=pd.DataFrame(mycursor.fetchall(),columns=["State","Pincodes","RegisteredUsers"])
        st.write(df9)
        fig_sunburst_9 = px.sunburst(df9, path=["State","Pincodes"], values="RegisteredUsers",
                                    title ="Total Phonepe Users")
        st.plotly_chart(fig_sunburst_9)
        st.subheader("Insights")
        st.write("Manipur has the lowest number of registered users with just 970 for pin code 795,009, while Tamil Nadu has the highest with 13,934 users for pin code 600,097. This indicates significant variation in user registrations across these states and pin codes")

    elif questions == "10.List the Payments and Types of Transactions conducted in each Union Territory using PhonePe":
        mycursor.execute('USE phonepae')
        mycursor.execute('''SELECT State,Transaction_type AS Transaction_Type, Transaction_amount AS Transaction_Amount  \
        FROM Agg_Trans \
        WHERE State in ("Ladakh","Jammu & Kashmir","Puducherry","Lakshadweep","Delhi","Chandigarh","Dadra and Nagar Have","Andaman and Nicobar Islands") \
        GROUP BY State \
        ORDER BY Transaction_Amount,Transaction_Type DESC \
        LIMIT 10''')
        df10=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Amount","Transaction_Type"])
        st.write(df10)
        fig_sunburst_10=px.sunburst(df10,path=["State","Transaction_Amount"],values="Transaction_Type",
                                title="Total Transactions and Type of Transacations")
        st.plotly_chart(fig_sunburst_10)
        st.subheader("Insights")
        st.write("Delhi leads in the total number of transactions, with a significant amount of ₹1.32 billion processed through Recharge & Bill Payments. Meanwhile, Jammu & Kashmir and Chandigarh follow with relatively lower transaction volumes but still significant amounts. It's notable that while Ladakh has a lower number of transactions, the average transaction amount is comparatively higher, suggesting potential opportunities for further analysis or targeted marketing efforts in these regions")

if select_options == "GEO VISUALIZATION":
    
    Year =st.slider("**Year**",min_value = 2018,max_value = 2023)
    Quarter =st.slider("**Quarter**",min_value = 1,max_value = 4)
    
    col1,col2=st.columns(2)
    with col1:
        st.markdown("## :violet[Overall State Transactions Amount]")
        geo_query1_df=f'''SELECT State,AVG(Transaction_amount) AS Transaction_Amount,AVG(Transaction_count) AS Transaction_Count FROM Map_Trans WHERE year =  {Year} AND quarter = {Quarter} GROUP BY State ORDER BY State'''
        
        mycursor.execute(geo_query1_df)

        geo_df1=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction_Amount","Transaction_Count"])

        fig_1 = px.choropleth(geo_df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='Reds')
    
        fig_1.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_1)
    
    with col2:
        st.markdown("## :violet[Overall State Total Transactions]")
    
        geo_query2_df=f'''SELECT State,AVG(Transaction_amount) AS Transaction_Amount,AVG(Transaction_count) AS Total_Transactions FROM Map_Trans WHERE year =  {Year} AND quarter = {Quarter} GROUP BY State ORDER BY State'''
        
        mycursor.execute(geo_query2_df)

        geo_df2=pd.DataFrame(mycursor.fetchall(),columns=["State","Transaction Amount","Total_Transactions"])

        fig_2 = px.choropleth(geo_df2,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Transactions',
                            color_continuous_scale='Reds')
    
        fig_2.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_2)

    #top 10 Brands
    st.markdown("### :violet[Top 10 Brands]")
    if (Year in [2018,2019,2020,2021,2022,2023] and Quarter in [1,2,3]) or (Year in [2022,2023] and Quarter in [4]):
        st.markdown("### Data is Not Available")
    else:
        y_query =f"""SELECT Brand,SUM(Transaction_count) AS Transaction_Count,AVG(Percentage)*100 AS AVG_Percentage From Agg_Users WHERE year =  {Year} AND quarter = {Quarter} GROUP BY Brand ORDER BY Transaction_Count DESC LIMIT 10"""
        mycursor.execute(y_query)
                                
        y_df1=pd.DataFrame(mycursor.fetchall(),columns=["Brand","Transaction_Count","AVG_Percentage"])
                        
        y_df1["Transaction_Count"] = y_df1["Transaction_Count"].astype(float)
        y_df1["AVG_Percentage"] = y_df1["AVG_Percentage"].astype(float)
                                
        fig_bar_brand = px.bar(y_df1,
                                title='Top 10',
                                x="Transaction_Count",
                                y="Brand",
                                orientation='h',
                                color="AVG_Percentage",
                                color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig_bar_brand,use_container_width=True)  
    
    
    # BAR CHART - TOP PAYMENT TYPE
    st.markdown("## :violet[Top Payment Type]")

    pay_query =f"""SELECT Transaction_type,SUM(Transaction_count) AS Transaction_Count,SUM(Transaction_amount) AS Transaction_Amount From Agg_Trans WHERE year =  {Year} AND quarter = {Quarter} GROUP BY Transaction_type ORDER BY Transaction_type"""
    mycursor.execute(pay_query)
                        
    pay_df1=pd.DataFrame(mycursor.fetchall(),columns=["Transaction_type","Transaction_Count","Transaction_Amount"])
        
    fig_bar_pay = px.bar(pay_df1,
                        title='Top 10',
                        x="Transaction_Count",
                        y="Transaction_type",
                        orientation='h',
                        color="Transaction_Amount",
                        color_continuous_scale=px.colors.sequential.Magenta)
            
    st.plotly_chart(fig_bar_pay,use_container_width=True)        
