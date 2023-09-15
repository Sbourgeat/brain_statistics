
#############################
##
##. Plotting data
##
############################
# Organise the data frame

library(GGally)
library(ggplot2)
library(rethinking)

cubical_entropy <- read.csv("/Users/skumar/Project/PHD_work/GWAS/dataset/vol_hratio.csv", header = TRUE) 
plot(cubical_entropy)



dat <- data.frame(Volume = cubical_entropy$h_ratio)
#dat$sex <- brain2$sex
dat$Volume <- standardize((dat$Volume))
dat$Entropy0 <-  standardize(exp(cubical_entropy$Entropy0))
dat$Entropy1 <-  standardize(exp(cubical_entropy$Entropy1))
dat$Entropy2 <-  standardize(exp(cubical_entropy$Entropy2))
dat$sex <- as.numeric(gsub("male", 1, gsub("female", 2, cubical_entropy$sex)))
dat$DGRP <- cubical_entropy$DGRP
#dat$log_E1 <- standardize(exp(cubical_entropy$Entropy1))

dat <- na.omit(dat)

dat <- dat[order(dat$abs_volume), ]



dat$DGRP_line <- as.factor(dat$DGRP)

dat$DGRP_line <- reorder(dat$DGRP_line, dat$Volume, FUN = mean)

cc_female <- dat[dat$sex == 2, ]
cc_male <- dat[dat$sex == 1, ]

# Create the plot

plot_graph <- function(cc_female, cc_male, dat) {
  jpeg(file="volume_h_ratio.jpeg",width=900, height=600)
  plot.new()
  
  plot(cc_female$DGRP_line, cc_female$Volume, lwd = 0.01, xlab = 'DGRP lines', 
       ylab = 'h_ratio', xaxt = 'n', frame = FALSE, col = F)
  
  axis(side = 1, at = 1:length(unique(dat$DGRP_line)), labels = unique(dat$DGRP_line), 
       cex.axis = 1, padj = 0.5)
  
  points(cc_female$DGRP_line, cc_female$Volume, lwd = 5, 
         col = rangi2, pch = 1)
  
  points(cc_male$DGRP_line, cc_male$Volume, lwd = 5, pch = 1, 
         col = 'darkred')
  
  # Add the legend
  legend("topleft", 
         legend = c("Female", "Male"), 
         col = c(rangi2, 'darkred'), 
         pch = c(1, 1), 
         lwd = c(5, 5),
         bty = "n", 
         pt.cex = 1, 
         cex = 1.2, 
         text.col = "black", 
         horiz = F)
  
  # Save the plot as pdf
  dev.off()
}

plot_graph(cc_female, cc_male, dat)
