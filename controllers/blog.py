from flask import *
from flask import request
from sqlalchemy import desc
from flask_login import current_user
from controllers.uploadfile import uploadfile
from models.blog import Postes,db

class blog:
    def newpost(request, app):
        try:
            data = request.form.to_dict()

            data['img'] = uploadfile(request, app)
            data['username'] = current_user.username
            # connection().insertinto('postes',
            #                         tuple([*data]),
            #                         tuple(data.values())).runquery()
            newpost = Postes(
                user_username=data['username'],
                title=data['title'],
                context=data['context'],
                img=data['img']
            )
            print(newpost)
            db.session.add(newpost)
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
