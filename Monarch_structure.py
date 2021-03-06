#install.packages(c("fields","RColorBrewer","mapplots"))
#paste -d "" 1 2 3 4 5 6 7 8 9 10 22 23 24 25 26 27 28 29 30 31 18 19 20 21 32 33 34 35 36 37 39 38 11 12 13 14 15 16 17 > ../plink.geno

source("http://bioconductor.org/biocLite.R")
biocLite("LEA")
install.packages("RColorBrewer")

library(RColorBrewer)

library(LEA)

jBrewColors <- c('#030303','#d90d0d')
V3<-c("HH1","HH2","HH3","HH4","HH5","HH6","HH7","HH8","HH9","HH10","PL1","PL2","PL4","PL5","PL6","PL7","PL8","PL9","PL10","ESB1","ESB2","ESB3","ESB4","ESB5","ESB6","ESB7","ESB8","ESB9","ESB10","stm163","stm146","T9","T14","NJ203","NJ116","NJ1","HI023","HI033","mex986","mex919","mex915","mex536","mex1527")


pdf(file= './new_struct' ,onefile=T,paper='A4', )

obj.snmf = snmf("plink.geno", K = 2:4, ploidy = 2, entropy = T,alpha = 100, project = "new")
plot(obj.snmf, col = "blue4", cex = 1.4, pch = 19)


obj.snmf = snmf("plink.geno", K = 2,  project = "new")
qmatrix1 = Q(obj.snmf, K = 2)
plot1=barplot(t(qmatrix1), col = jBrewColors, border = NA, ylab = "K=2")

dev.off()

jBrewColors <- c('#d90d0d','#f4b400','#5668ba','#030303')
pdf(file= './Addmixture_4.pdf' ,onefile=T,paper='A4', )
obj.snmf = snmf("plink.geno", K = 4,  project = "new")
qmatrix1 = Q(obj.snmf, K = 4)

plot1=barplot(t(qmatrix1), col = jBrewColors, border = NA, ylab = "K=2")

dev.off()


######################################end of ploting###############

obj.snmf1 = snmf("plink.geno", K = 3,  project = "new")
  qmatrix1 = Q(obj.snmf1, K = 3)
   #qmat2 <- qmatrix1[order(qmatrix1[,1]),]
plot1=barplot(t(qmatrix1), col = jBrewColors, border = NA, ylab = "K=3")


obj.snmf2 = snmf("plink.geno", K = 4,  project = "new")
  qmatrix2 = Q(obj.snmf2, K = 4)
  #qmat2 <- qmatrix1[order(qmatrix1[,1]),]
plot1=barplot(t(qmatrix2), col = jBrewColors, border = NA, ylab = "K=4")


obj.snmf3 = snmf("plink.geno", K = 5,  project = "new")
  qmatrix3 = Q(obj.snmf3, K = 5)
  #qmat2 <- qmatrix1[order(qmatrix1[,1]),]
plot1=barplot(t(qmat2), col = jBrewColors, border = NA, ylab = "K=5")

obj.snmf4 = snmf("plink.geno", K = 6,  project = "new")
  qmatrix4 = Q(obj.snmf4, K = 6)
  qmat2 <- qmatrix1[order(qmatrix1[,1]),]
plot1=barplot(t(qmat2), col = jBrewColors, border = NA, ylab = "K=6")

obj.snmf5 = snmf("plink.geno", K = 7,  project = "new")
  qmatrix5 = Q(obj.snmf5, K = 7)
plot5=barplot(t(qmatrix5), col = jBrewColors, border = NA, ylab = "K=7")

obj.snmf6 = snmf("plink.geno", K = 6,  project = "new")
  qmatrix6 = Q(obj.snmf6, K = 6)
plot6=barplot(t(qmatrix6), col = jBrewColors, border = NA, ylab = "K=8")


obj.snmf7 = snmf("plink.geno", K = 9,  project = "new")
  qmatrix7 = Q(obj.snmf7, K = 9)
plot7=barplot(t(qmatrix7), col = jBrewColors, border = NA, ylab = "K=9")
