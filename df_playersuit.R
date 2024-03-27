library(worldfootballR)
library(dplyr)

#create data frame

pacho_def <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "defense")
pacho_sho <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "shooting")
pacho_pass <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "passing")
pacho_pt <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "passing_types")
pacho_poss <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "possession")
pacho_misc <- fb_player_season_stats("https://fbref.com/en/players/ecbe2839/Willian-Pacho", stat_type = "misc")

pacho_stats<-list(pacho_def, pacho_sho, pacho_pass, pacho_pt, pacho_poss, pacho_misc)

#trimming
pacho_stats[[1]]=select(pacho_stats[[1]], -2,-5:-7)
pacho_stats[[2]]=select(pacho_stats[[2]], -2,-5:-7)
pacho_stats[[3]]=select(pacho_stats[[3]], -2,-5:-7)
pacho_stats[[4]]=select(pacho_stats[[4]], -2,-5:-7)
pacho_stats[[5]]=select(pacho_stats[[5]], -2,-5:-7)
pacho_stats[[6]]=select(pacho_stats[[6]], -2,-5:-7,-9:-17)
# dfcheck<-df(pacho_stats[[1]])
# dfcheck<-df(pacho_stats[[2]])
# dfcheck<-df(pacho_stats[[3]])
# dfcheck<-df(pacho_stats[[4]])
# dfcheck<-df(pacho_stats[[5]])
# dfcheck<-df(pacho_stats[[6]])

#fill missing value
for (i in 1:6){
  pacho_stats[[i]] <- pacho_stats[[i]] %>% replace(is.na(.), 0)
  # checkna <- which(is.na(list[[i]][,8:length(list[[i]])]))
  # print(checkna)
}
pstats<-full_join(pacho_stats[[1]],pacho_stats[[2]])
pstats<-full_join(pstats,pacho_stats[[3]])
pstats<-full_join(pstats,pacho_stats[[4]])
pstats <-full_join(pstats,pacho_stats[[5]])
pstats <-full_join(pstats,pacho_stats[[6]])
pstats<-data.frame(pstats)


