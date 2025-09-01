
import rsa
import flask
import boto3
import pymysql

app = flask.Flask(__name__)

db_host = "db-url"
db_user = 'MyUser'
db_password = 'Enter your password'
db_name = 'Encryption'
db_port = 3306
@app.route('/')
def index():
    return flask.render_template('homepage.html')


@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    word = flask.request.form.get('text')
    publickey, privatekey = rsa.newkeys(1024)
    enc = rsa.encrypt(str(word).encode('utf-8'), publickey)
    print(enc)

    try:
        connection = pymysql.connect(host=db_host,
                                     user=db_user,
                                     password=db_password,
                                     db=db_name,
                                     port=db_port)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Encryption")
        create_table_sql = """
    CREATE TABLE IF NOT EXISTS EncryptionTable (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Text VARCHAR(255) NOT NULL,
        Encrypted VARCHAR(255) NOT NULL
    );
    """
        
        cursor.execute(create_table_sql)
        
        insert_sql = "INSERT INTO EncryptionTable (Text, Encrypted) VALUES ('word', 'enc')"
        cursor.execute(insert_sql)
        connection.commit()
        cursor.close()
        connection.close()

    except Exception as e:
        print(e)

    finally:
        return flask.render_template('homepage.html', word=word, enc=enc)




if __name__ == '__main__':
    app.run(debug=True)