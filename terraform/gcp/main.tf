terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.60.1"
    }
  }
}

provider "google" {
  project = var.project_name
  region  = var.region
  zone    = var.zone
}
