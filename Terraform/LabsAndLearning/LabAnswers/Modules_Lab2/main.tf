module "website_s3_bucket" {
  source = "./modules/terraform-aws-s3website"

  bucket_name = "<UNIQUE BUCKET NAME>"

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}