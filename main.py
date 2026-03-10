from flask import Flask, render_template

app = Flask("Book Store", static_folder="static")


@app.route("/")
def home():

    # List of books
    books = [
        "Harry Poter",
        "Lord of the rings",
        "The titanic"
    ]

    # Dictionary
    data = {
        "book_list" : books,
        "key" : "Yinhla Makamu"
    }


    return render_template("index.html", **data)


@app.route("/book-list")
def book_list():
    return render_template("booklist.html") 



@app.route("/contact")
def contact():
    return render_template("contactus.html") 


@app.route("/help")
def help():
    return render_template("help.html") 


# Main file to be executed
if __name__ == "__main__":
    # starting point of my application

    app.run(debug=True)
