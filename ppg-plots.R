library(tidyverse)
library(ggplot2)
library(ggdark)


fps <- 29.97*2

folder <- 'D:/GitHub/kitahack-2023/output-data-faw_preprocess.mp4-2'

read_ppg <- function(filename, fps) {
    read_csv(filename) %>%
        mutate(t = (1:n())/fps)
}

rgb <-
    read_ppg(
        file.path(folder, 'ppg-rgb.csv'),
        fps
    )

ggplot(rgb, aes(x=t)) +
    geom_line(aes(y=r), colour='red') +
    geom_line(aes(y=g), colour='green') +
    geom_line(aes(y=b), colour='blue') +
    dark_theme_bw()

rgb_ma <-
    read_ppg(
        file.path(folder, 'ppg-rgb-ma.csv'),
        fps
    )

ggplot(rgb_ma, aes(x=t)) +
    geom_line(aes(y=r), colour='red') +
    geom_line(aes(y=g), colour='green') +
    geom_line(aes(y=b), colour='blue') +
    dark_theme_bw() +
    coord_cartesian(
        xlim = c(10, 19),
        ylim = c(-0.0025, 0.0025),
        expand = TRUE
    )


yuv <-
    read_ppg(
        file.path(folder, 'ppg-yuv.csv'),
        fps
    )

ggplot(yuv, aes(x=t)) +
    geom_line(aes(y=y), colour='white') +
    geom_line(aes(y=u), colour='green') +
    geom_line(aes(y=v), colour='magenta') +
    dark_theme_bw()



yuv_ma <-
    read_ppg(
        file.path(folder, 'ppg-yuv-ma.csv'),
        fps
    )

ggplot(yuv_ma, aes(x=t)) +
    geom_line(aes(y=y), colour='grey50') +
    geom_line(aes(y=u), colour='green') +
    geom_line(aes(y=v), colour='magenta') +
    dark_theme_bw() +
    coord_cartesian(
        xlim = c(10, 19),
        ylim = c(-0.0025, 0.0025),
        expand = TRUE
    )


ggplot(yuv_ma, aes(x=t)) +
  geom_line(aes(y=r), data=rgb_ma, colour='green') +
  dark_theme_bw() +
  coord_cartesian(
    xlim = c(10, 19),
    ylim = c(-0.0025, 0.0025),
    expand = TRUE
  )



welch <-
  read_csv(
    file.path(folder, 'latest_ecg.csv'),
  col_names=FALSE
)

ggplot(welch, aes(x=X1, y=X2)) +
  geom_line(colour='black')




ecg <- read_delim(
  'ecg_text.txt',
  delim=';'
  )

ecg <-
  ecg %>%
  mutate(
    t = `timestamp [ms]`/1000 + 4 + 33/59.94 - 16 - 56/59.94
  )

ggplot(ecg, aes(x=t, y=`ecg [uV]`)) +
  geom_line(colour='red') +
  geom_line(data=rgb_ma, aes(y=g*1e5), colour='green') +
  dark_theme_bw() +
  coord_cartesian(
    xlim = c(20, 30),
    ylim = c(-1000, 2500),
    expand = TRUE
  )

