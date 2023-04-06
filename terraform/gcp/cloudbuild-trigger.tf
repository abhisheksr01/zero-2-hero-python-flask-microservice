resource "google_cloudbuild_trigger" "zero_to_hero_pipeline_trigger" {
  description     = "gcloud build trigger for zero to hero repo"
  filename        = "cloudbuild.yaml"
  location        = var.region
  name            = "${var.resource_name_prefix}-pipeline-trigger"
  project         = var.project_name
  service_account = google_service_account.cloudbuild_service_account.name
  tags = [
    "environment=dev", "owner=abhisheksr01", "provisioner=terraform"
  ]

  approval_config {
    approval_required = false
  }

  github {
    name  = var.repository_name
    owner = var.repository_owner

    push {
      branch       = "^main$"
      invert_regex = false
    }
  }

}
