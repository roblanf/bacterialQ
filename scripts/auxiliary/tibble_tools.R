library(tibble)
library(dplyr)

#' @description
#' This function removes symmetric pairs from a dataframe. It takes two columns, sorts the values in each row,
#' and removes duplicate rows based on the sorted values.
#' @param df A dataframe containing the data.
#' @param col1 The name of the first column to consider for symmetric pairs.
#' @param col2 The name of the second column to consider for symmetric pairs.
#' @return A dataframe with symmetric pairs removed.
remove_symmetric <- function(df, col1, col2) {
  df <- df %>%
    mutate(AB_sorted = apply(df[c(col1, col2)], 1, function(x) paste(sort(x), collapse = ""))) %>%
    distinct(AB_sorted, .keep_all = TRUE) %>%
    select(-AB_sorted)
  return(df)
}

# Define the function
#' @description
#' This function takes a dataframe and two column names, generates a symmetric copy of the dataframe
#' @param df A dataframe.
#' @param col1 A string representing the name of the first column.
#' @param col2 A string representing the name of the second column.
#' @return A dataframe with the original and symmetric rows.
symmetric_bind <- function(df, col1, col2) {
  # Check if the specified columns exist in the dataframe
  if (!(col1 %in% colnames(df)) | !(col2 %in% colnames(df))) {
    stop("Specified columns do not exist in the dataframe")
  }

  # Generate the symmetric copy by swapping col1 and col2
  symmetric_df <- df %>%
    mutate(!!col1 := df[[col2]], !!col2 := df[[col1]])

  # Bind the original dataframe with the symmetric dataframe
  result_df <- bind_rows(df, symmetric_df)

  return(result_df)
}
