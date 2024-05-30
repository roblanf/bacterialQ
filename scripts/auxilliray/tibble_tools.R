library(tibble)
library(dplyr)

remove_symmetric <- function(df, col1, col2) {
  df <- df %>%
    mutate(AB_sorted = apply(df[c(col1, col2)], 1, function(x) paste(sort(x), collapse = ""))) %>%
    distinct(AB_sorted, .keep_all = TRUE) %>%
    select(-AB_sorted)
  return(df)
}
