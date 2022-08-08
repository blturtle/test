import pymysql
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='web_test', charset="utf8")
cursor = db.cursor()

@app.route("/page", methods=["GET"])
def hello():
    return render_template('index.html')

@app.route("/student", methods=["GET"])
def get_scores():
    sql = "select * from student_score"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    students = []
    for result in results:
        students.append({
            'name': result[0],
            'korean_s': result[1],
            'mathmatics_s': result[2],
            'english_s': result[3]
        })
    return jsonify(students)

@app.route("/student", methods=["POST"])
def save_score():
    server_name = request.form["name"]
    server_korean = request.form["korean_s"]
    server_mathmatics = request.form["mathmatics_s"]
    server_english = request.form["english_s"]
    sql = "insert into student_score (name, korean_s, mathmatics_s, english_s) values ('%s', %s, %s, %s)" % (server_name, server_korean, server_mathmatics, server_english)
    cursor.execute(sql)
    db.commit()
    return "OK"

@app.route("/student", methods=["DELETE"])
def delete_score():
    server_name = request.args.get("name")
    sql = "delete from student_score where name = '%s'" % server_name
    cursor.execute(sql)
    db.commit()
    return "OK"

@app.route("/student", methods=["PUT"])
def update_score():
    server_name = request.form["name"]
    server_korean = request.form["korean_s"]
    server_mathmatics = request.form["mathmatics_s"]
    server_english = request.form["english_s"]
    sql = "update student_score set korean_s = %s, mathmatics_s = %s, english_s = %s where name = '%s'" % (server_korean, server_mathmatics, server_english, server_name)
    cursor.execute(sql)
    db.commit()
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)