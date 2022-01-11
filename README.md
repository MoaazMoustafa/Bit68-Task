# Instructions to run the code

- Clone the repo from github
- Create your virtual environment
- Run pip install -r requeriments.txt
- Make sure to configure your database You have to create a postgresql database with the same name and the same user and password or You can use sqlite3 database if you like.
- Here are the endpoints

## APIs

### accounts/signup/

- To register an new account you have to enter the username, email, password and confirm_password
- If the account created successfully the response will be the user data and a token created once the account created and a message tells you that you have successfully registered
- If there is anything wrong happens the response will be the error that happend

### accounts/login/

- The response will be the token of the loged in user

### product/list/

- This endpoint will return all the products in the database but the user must be authenticated and the token must be provided in the headers of the request

### product/details/id

- This endpoint will return a product with a specific id which is given in the url but the user must be authenticated and the token must be provided in the headers of the request

### product/create/

- This endpoint will create a product. The body of the request must contain the name and the price of the product and the user who sends the request will be the seller of the product so he has to be authenticated so the token must be sent within the headers of the request
