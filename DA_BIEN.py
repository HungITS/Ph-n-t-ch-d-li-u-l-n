import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# Nhập dữ liệu đầu vào
df = pd.read_csv('dataset.csv')
import plotly.express as px

#Biểu đồ phân phối giá nhà theo khu vực
quan = px.box(data_frame = df,
       x = 'Quan',
       y = 'Gia',
       color = 'Quan',
       title = 'Biểu đồ phân bố Giá nhà theo khu vực',
       labels = {'Quan' : 'Quan'})
quan.show()

#Thống kê mô tả giá theo khu vực
t = df.groupby('Quan').agg({'Gia':['count', 'mean', 'std','min','max',lambda  x: x.quantile(0.25),lambda  x: x.quantile(0.5),lambda  x: x.quantile(0.75),lambda  x: x.quantile(0.75)- x.quantile(0.25)]}).reset_index()
t.columns = ['Huyen','count', 'mean', 'std','min','max','Q1','Q2','Q3','IQR']
print(t)
#Biểu đồ  phân phối giá nhà theo số lượng phòng ngủ.
pn = px.box(data_frame = df,
       x = 'Phongngu',
       y = 'Gia',
       color = 'Phongngu',
       title = 'Biểu đồ phân bố Giá nhà theo Phòng ngủ',
       labels = {'Phongngu' : 'Phongngu'})
pn.show()

#Biểu đồ  phân phối giá nhà theo Loại chung cư.
l = px.box(data_frame = df,
       x = 'Loai',
       y = 'Gia',
       color = 'Loai',
       title = 'Biểu đồ phân bố Giá nhà theo Loại chung cư',
       labels = {'Loai' : 'Loai'})
l.show()
#Thống kê mô tả giá theo loại chung cư
n = df.groupby('Loai').agg({'Gia':['count', 'mean', 'std','min','max',lambda  x: x.quantile(0.25),lambda  x: x.quantile(0.5),lambda  x: x.quantile(0.75),lambda  x: x.quantile(0.75)- x.quantile(0.25)]}).reset_index()
n.columns = ['Loai','count', 'mean', 'std','min','max','Q1','Q2','Q3','IQR']
print(n)
#Biểu đồ  phân phối giá nhà theo tình trạng nội thất.
tt = px.box(data_frame = df,
       x = 'TinhTrangNoiThat',
       y = 'Gia',
       color = 'TinhTrangNoiThat',
       title = 'Biểu đồ phân bố Giá nhà theo tình trạng nội thất',
       labels = {'TinhTrangNoiThat' : 'TinhTrangNoiThat'})
tt.show()

#Biểu đồ  phân phối giá nhà theo giấy tờ đất.
gt = px.box(data_frame = df,
       x = 'GiayTo',
       y = 'Gia',
       color = 'GiayTo',
       title = 'Biểu đồ phân bố Giá nhà theo Giấy tờ đất',
       labels = {'GiayTo' : 'GiayTo'})
gt.show()

#Biểu đồ giá nhà bị ảnh hưởng bởi diện tích.
dientich = px.scatter(df,
                 x='DienTich',
                 y='Gia',
                 title='Biểu đồ mức độ phụ thuộc của Giá vào Diện tích',
                 labels={'DienTich': 'DienTich (m²)', 'Gia': 'Gia (Tỉ VNĐ)'},
                 color='Gia')
dientich.show()

#Biểu đồ Scatter thể hiện giá nhà ảnh hưởng bởi khu vực và diện tích.
sca = px.scatter(data_frame=df,
       x='Quan',
       y='DienTich',
       color='Gia',
       size='Gia', opacity=0.5,
       labels={'Quan': 'Khu vực', 'DienTich': 'Diện tích',
       'Gia': 'Giá nhà'},
       hover_data=['Gia'],
       title='BIỂU ĐỒ GIÁ NHÀ ẢNH HƯỞNG BỞI KHU VỰC VÀ DIỆN TÍCH CHUNG CƯ')
sca.show()

# Biểu đồ bar chart phân bổ khu vực và tình trạng nội thất
plt.figure(figsize=(12, 4))
sns.countplot(data=df, x='Quan', hue='TinhTrangNoiThat')
plt.title('Biểu đồ bar chart phân bổ khu vực và tình trạng nội thất')
plt.xticks(rotation=45)
# Biểu đồ bar chart phân bổ khu vực và loại chung cư
plt.figure(figsize=(12, 4))
sns.countplot(data=df, x='Quan', hue='Loai')
plt.title('Biểu đồ bar chart phân bổ khu vực và loại chung cư')
plt.xticks(rotation=45)
plt.show()

