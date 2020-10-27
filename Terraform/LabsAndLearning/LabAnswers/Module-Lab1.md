# Module - Lab 1

1.Fork the repository
2.Create local terraform project (main.tf file)

```hcl
module "website_s3_bucket" {
  source = "github.com/Keimille/terraform-aws-s3website"

  bucket_name = "<UNIQUE BUCKET NAME>"

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

3.Run `terraform init`
4.Run `terraform plan`
