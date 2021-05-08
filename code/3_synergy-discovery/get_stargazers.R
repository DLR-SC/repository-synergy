require(httr)
require(dplyr)
require(jsonlite)

get_stargazers <- function(repo_url) {
  
  tryCatch({
    GET(
      paste0(repo_url, "/stargazers"), 
      add_headers(Accept="application/vnd.github.mercy-preview+json")
    ) %>% 
      content %>%
      lapply(dplyr::as_data_frame) %>%
      do.call(bind_rows, .)
  }, 
  error = function(e) {
    
    print(paste("Problems with", repo_url))
    print(e)
    NULL
  })
}