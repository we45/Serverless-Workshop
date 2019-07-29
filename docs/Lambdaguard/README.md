# LambdaGuard

* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/`

```commandline
cd /root/labs/Serverless-Workshop/
```
* Step 2: Run `lambdaguard --region=us-west-2` you might have to substitute `us-west-2` for any other region you have deployed your serverless functions in

```commandline
lambdaguard --region=us-west-2
```
 
* Wait for Lambdaguard to complete analysis
* Step 3: Now run: 

```bash
python -m http.server
```

* Step 4: In another browser tab, go to the URL for your image followed by port 8000 `<url for your image>:8000`

* Step 5: Open up the report in `Lambdaguard output` directory 
