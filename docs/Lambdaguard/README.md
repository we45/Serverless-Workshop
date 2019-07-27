# LambdaGuard

* In your image, navigate over to `/root/labs/Serverless-Workshop/`
* Run `lambdaguard --region=us-west-2` you might have to substitute `us-west-2` for any other region you have deployed your serverless functions in 
* Wait for Lambdaguard to complete analysis
* Now run: 

```bash
python -m http.server
```

* In another browser tab, go to the URL for your image followed by port 8000 `<url for your image>:8000`
* Open up the report in Lambdaguard output directory 
