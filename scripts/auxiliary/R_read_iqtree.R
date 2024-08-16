library(readr)
library(dplyr)
library(stringr)

#' Extract model information from the IQ-TREE output file
#'
#' @description This function reads an IQ-TREE output file and extracts model information, returning it as a tibble.
#' @param iqtree_file Path to the IQ-TREE output file.
#' @return A tibble containing model name, LogL, and BIC.
extract_iqtree_model_table <- function(file_path) {
  file_content <- readLines(file_path)

  start_line <- which(str_detect(file_content, "List of models sorted by BIC scores:")) + 1
  end_line <- which(str_detect(file_content, "AIC, w-AIC   : Akaike information criterion scores and weights.")) - 1

  table_content <- file_content[start_line:end_line]

  table_content <- str_replace_all(table_content, " \\+ ", " ")
  table_content <- str_replace_all(table_content, " - ", " ")
  table_content <- str_replace_all(table_content, "\\s+", ",")

  df <- read.csv(text = paste(table_content, collapse = "\n"), header = TRUE)
  df <- select(df, Model, LogL, AIC, AICc, BIC)

  return(df)
}


#' Extract model information from the partitioned IQ-TREE output file
#'
#' @description This function reads a partitioned IQ-TREE output file and extracts model information, returning it as a tibble.
#' @param best_scheme_file Path to the best scheme file of IQ-TREE output.
#' @param output_dir Output directory for test results.
#' @return A tibble containing model counts.
extract_model_info_partition <- function(best_scheme_file, output_dir) {
  model_data <- get_and_print_model_counts(best_scheme_file, file.path(output_dir, "model_counts.txt"))
  model_counts <- tibble(
    Model = names(model_data),
    Count = unname(model_data)
  )
  return(model_counts)
}


#' Parse model string and extract components
#'
#' @description This function parses a model string column in a data frame and extracts specific components, adding new columns to the data frame based on the presence of certain patterns in the model string.
#' @param data A data frame containing the model string column.
#' @param model_string_col The name of the column in the data frame that contains the model string.
#' @return A data frame with additional columns for Q_matrix, state_freq, invariant_site, and RHAS.
parse_model_string <- function(data, model_string_col) {
  # Extract the Q_matrix from the model string if it contains a '+', otherwise use the entire model string
  data <- data %>%
    mutate(Q_matrix = ifelse(str_detect(!!sym(model_string_col), "\\+"), 
                             str_extract(!!sym(model_string_col), "^[^+]+"), 
                             !!sym(model_string_col)))

  # Detect the presence of '+F+' in the model string and set state_freq to 'FO' if present, otherwise 'FE'
  data <- data %>%
    mutate(state_freq = ifelse(str_detect(!!sym(model_string_col), "\\+F\\+"), "FO", "FE"))

  # Detect the presence of '+I+' in the model string and set invariant_site to TRUE if present, otherwise FALSE
  data <- data %>%
    mutate(invariant_site = ifelse(str_detect(!!sym(model_string_col), "\\+I\\+"), TRUE, FALSE))

  # Extract the RHAS value from the model string if it matches the pattern '+R' or '+G' followed by digits
  # Remove the leading '+' from the extracted value, or set to NA if not present
  data <- data %>%
    mutate(RHAS = str_extract(!!sym(model_string_col), "\\+[RG]\\d+"),
           RHAS = ifelse(!is.na(RHAS), str_remove(RHAS, "^\\+"), NA))

  return(data)
}