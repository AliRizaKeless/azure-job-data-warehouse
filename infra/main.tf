provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "job-data-rg"
  location = "Norway East"
}

resource "azurerm_storage_account" "storage" {
  name                     = "jobdatastorage12345"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "container" {
  name                  = "raw-data"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}