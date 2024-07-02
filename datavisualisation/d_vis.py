import matplotlib.pyplot as plt

ypoints = [2,5,7,4,6,5,3]
xpoints = [2,3,4,5,6,7,8]

plt.plot(xpoints,ypoints, marker='o')

xpoints = [1, 2, 3]
ypoints = [1, 2, 3]
plt.plot(xpoints,ypoints, marker = 'X',linestyle='--',markerfacecolor='yellow', color='red',markersize=25)
plt.xticks([3,5,7])
plt.show()

# pasta grafiği oluşturma
degerler = [20,25,15,10,30]
kategoriler = ["Teknoloji","Giyim","Kozmetik","Ulaşım","Gıda"]
renkler = ["#B32428","#A98307","#F4F4F4","#015D52","#8B8C7A"]

plt.pie(degerler, labels=kategoriler,colors=renkler)

plt.show()


# aylara göre login grafiği 
x = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos"]
y = [1000,3000,2500,700,0,0,0,0]
plt.bar(x,y,color="red")
plt.title("Aylara Göre Login Grafiği")
plt.xlabel("Ay")
plt.ylabel("Kişi Sayısı")

plt.show()

y = [3,4,5,6,7,1,4,5]
plt.subplot(2,1,1)
plt.plot(y)


#---
plt.subplot(2,2,3)
plt.plot()

y = [5,4,3,1]
plt.subplot(2,2,4)
plt.plot(y)

plt.show()