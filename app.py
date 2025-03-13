from flask import Flask, jsonify

todo = Flask(__name__)
students = [
    {
        'id':1,
        'name':'harish',
        'age':10
    },
{
        'id':2,
        'name':'hemanth',
        'age':12
    },
{
        'id':3,
        'name':'pramod',
        'age':14
    }
]
@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
        print(std)

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )
