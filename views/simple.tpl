<html>
    <head> <title> {{title}} </title> </head>
    <style>
    .footer {
       position: fixed;
       left: 0;
       bottom: 0;
       width: 100%;
       border-top: 1px solid;
       color: black;
       text-align: center;
    }
    input[type=text] {
        width: 100%;
    }
    input[type=text]:focus {
        background-color: lightblue;
    }
    input[type=button], input[type=submit], input[type=reset] {
        background-color: #4CAF50;
  border: none;
  color: white;
  padding: 16px 32px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
    }


    </style>

    <body>
        <h1> {{title}} </h1>
        {{content}}<br>

        <form method="post">
            Start page: <input name="start" type="text" />
            End page: <input name="end" type="text" value="Kevin Bacon" />
            <input value="Find" type="submit" />
        </form>

    <div class="footer">
        Made by <a href=https://github.com/lucaspauker>Lucas Pauker</a> and <a href=https://github.com/TheShashank>Shashank Rammorthy</a>
    </div>
    </body>
</html>

