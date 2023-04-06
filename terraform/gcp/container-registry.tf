resource "google_artifact_registry_repository" "zero_to_hero_ci_artifactory" {
  project       = var.project_name
  repository_id = "${var.resource_name_prefix}-registry"
  format        = "DOCKER"
  location      = var.region
}
