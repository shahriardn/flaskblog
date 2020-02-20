from flask import *
from flask import request
from sqlalchemy import desc, update
from flask_login import current_user
from controllers.uploadfile import uploadfile
from models.blog import Postes, db


class blog:
    def newpost(request, app):
        try:
            data = request.form.to_dict()

            data['img'] = uploadfile(request, app)
            data['username'] = current_user.username
            newpost = Postes(
                user_username=data['username'],
                title=data['title'],
                context=data['context'],
                img=data['img']
            )
            db.session.add(newpost)
            db.session.commit()
            return True
        except Exception as error:
            print('errorrrrrrrrrrrrrr issssssss', error)
            return {"error": error}

    def deletepost(id, username):
        try:
            db.session.query(Postes).filter_by(
                id=id,
                user_username=username).delete()
            db.session.commit()
            return True
        except Exception as error:
            print('errorrrrrrrrrrrrrr issssssss', error)
            return {"error": error}

    def updatepost(request, app):
        try:
            data = request.form.to_dict()
            if 'img' in data.keys():
                data['img'] = uploadfile(request, app)
            else:
                data['img'] = data['lastfile']
            data['username'] = current_user.username
            updatepost = Postes.query.filter_by(
                id=data['id']).first()
            updatepost.title = data['title']
            updatepost.context = data['context']
            updatepost.img = data['img']
            db.session.commit()
            return True
        except Exception as error:
            print('errorrrrrrrrrrrrrr issssssss', error)
            return {"error": error}

    def show_index():
        paginatedpostes = Postes.query.order_by(desc(Postes.id)).all()

        context = {
            'postes': [paginatedpostes[i:i+3] for i in range(0, len(paginatedpostes), 3)],
            'user': current_user.username
        }
        return render_template("blog/index.html", context=context)
