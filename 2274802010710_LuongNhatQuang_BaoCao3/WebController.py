from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.secret_key = 'N1h3a0t1Q2u0a0n4g'

login_manager = LoginManager() 
login_manager.init_app(app) 
login_manager.login_view = "dangnhap"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:130104@localhost:5432/QuanLyNhanSu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class NhanVien(db.Model): 
    __tablename__ = 'nhanvien' 
    id = db.Column(db.String(50), primary_key=True)
    hoten = db.Column(db.String(255), nullable=False) 
    luongcoban = db.Column(db.Integer, nullable=False) 
    songaylamviec = db.Column(db.Integer, nullable=False) 
    trocap = db.Column(db.Integer, nullable=False)
    luong = db.Column(db.Integer, nullable=False)

class QuanLy(db.Model): 
    __tablename__ = 'quanly' 
    id = db.Column(db.String(50), primary_key=True)
    hoten = db.Column(db.String(255), nullable=False) 
    luongcoban = db.Column(db.Integer, nullable=False)
    hesochucvu = db.Column(db.Float, nullable=False)
    thuong = db.Column(db.Integer, nullable=False)
    luong = db.Column(db.Integer, nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = 'taikhoan' 
    id = db.Column(db.Integer, primary_key=True) 
    usr = db.Column(db.String, nullable=False) 
    passwd = db.Column(db.String, nullable=False)

class Website:
    def __init__(self):
        self.web = app
        self.Setup_Route()

    def Setup_Route(self):
        @login_manager.user_loader 
        def load_user(id):
            return User.query.get(id)
        
        @self.web.route("/dangnhap", methods=['GET', 'POST'])
        def dangnhap():
            if request.method == 'POST':
                username = request.form.get("usr")
                password = request.form.get("pwd")
                user = User.query.filter_by(usr=username).first()
                if user and user.passwd == password:
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    return redirect(url_for('dangnhap'))
            return render_template("dangnhap.html")
        
        @self.web.route("/dangxuat")
        @login_required
        def dangxuat():
            logout_user()
            return redirect(url_for('dangnhap'))

        @self.web.route("/")
        @login_required
        def index():
            employees = NhanVien.query.all()
            managers = QuanLy.query.all()

            return render_template("index.html",search_employee=None, search_manager=None, employees=employees, managers=managers, user=current_user)
        
        @self.web.route("/nhanvien", methods=["GET", "POST"])
        @login_required
        def nhanvien():
            if request.method == "POST":
                try:
                    id = request.form.get("InputID")
                    name = request.form.get("InputName") 
                    basic_salary = int(request.form.get("InputBasicSalary")) 
                    work_day = int(request.form.get("InputWorkDay") )
                    subsidy = int(request.form.get("InputSubsidy"))
                    salary = basic_salary + work_day * 200000 + subsidy
                    
                    new_employee = NhanVien(id=id, hoten=name, luongcoban=basic_salary, songaylamviec=work_day, trocap=subsidy, luong=salary)
                    db.session.add(new_employee) 
                    db.session.commit()
                    return redirect(url_for("nhanvien"))
                except IntegrityError:
                    db.session.rollback()
                except ValueError:
                    pass
            return render_template("luongnhanvien.html", user=current_user)
        
        @self.web.route("/get_employee/<string:id>")
        @login_required
        def get_employee(id): 
            employee = NhanVien.query.get(id) 
            if employee: 
                return jsonify({ 
                    'id': employee.id, 
                    'hoten': employee.hoten, 
                    'luongcoban': employee.luongcoban, 
                    'songaylamviec': employee.songaylamviec, 
                    'trocap': employee.trocap 
                    }) 
            return jsonify({'error': 'Nhân viên không tồn tại'}), 404 
        
        @self.web.route("/update_employee", methods=["POST"])
        @login_required
        def update_employee(): 
            employee_id = request.form.get("employee_id") 
            employee = NhanVien.query.get(employee_id) 
            if employee: 
                employee.hoten = request.form.get("UpdateName_Employee") 
                employee.luongcoban = int(request.form.get("UpdateBasicSalary_Employee")) 
                employee.songaylamviec = int(request.form.get("UpdateWorkDay_Employee")) 
                employee.trocap = int(request.form.get("UpdateSubsidy_Employee")) 
                employee.luong = employee.luongcoban + employee.songaylamviec * 200000 + employee.trocap 
                
                db.session.commit() 
                return redirect(url_for("index")) 
            return "Nhân viên không tồn tại", 404
    
        @self.web.route("/delete_employee/<string:id>")
        @login_required
        def delete_employee(id): 
            employee = NhanVien.query.get_or_404(id) 
            db.session.delete(employee) 
            db.session.commit() 
            return redirect(url_for("index"))

        @self.web.route("/quanly", methods=["GET", "POST"])
        @login_required
        def quanly():
            if request.method == "POST":
                try:
                    id = request.form.get("InputID")
                    name = request.form.get("InputName") 
                    basic_salary = int(request.form.get("InputBasicSalary")) 
                    position_coefficient = float(request.form.get("InputPositionCoefficient") )
                    bonus = int(request.form.get("InputBonus"))
                    salary = basic_salary * position_coefficient + bonus

                    new_manager = QuanLy(id=id, hoten=name, luongcoban=basic_salary, hesochucvu=position_coefficient, thuong=bonus, luong=salary)
                    db.session.add(new_manager) 
                    db.session.commit()
                    return redirect(url_for("quanly"))
                except IntegrityError:
                    db.session.rollback()
                except ValueError:
                    pass
            return render_template("luongquanly.html", user=current_user)
        
        @self.web.route("/get_manager/<string:id>")
        @login_required
        def get_manager(id): 
            manager = QuanLy.query.get(id) 
            if manager: 
                return jsonify({ 
                    'id': manager.id, 
                    'hoten': manager.hoten, 
                    'luongcoban': manager.luongcoban, 
                    'hesochucvu': manager.hesochucvu, 
                    'thuong': manager.thuong 
                    }) 
            return jsonify({'error': 'Quản lý không tồn tại'}), 404 
        
        @self.web.route("/update_manager", methods=["POST"])
        @login_required
        def update_manager(): 
            manager_id = request.form.get("manager_id") 
            manager = QuanLy.query.get(manager_id) 
            if manager: 
                manager.hoten = request.form.get("UpdateName_Manager") 
                manager.luongcoban = int(request.form.get("UpdateBasicSalary_Manager")) 
                manager.hesochucvu = float(request.form.get("UpdatePositionCoefficient_Manager")) 
                manager.thuong = int(request.form.get("UpdateBonus_Manager")) 
                manager.luong = manager.luongcoban * manager.hesochucvu + manager.thuong
                
                db.session.commit() 
                return redirect(url_for("index")) 
            return "Quản lý không tồn tại", 404
        
        @self.web.route("/delete_manager/<string:id>")
        @login_required
        def delete_manager(id): 
            manager = QuanLy.query.get_or_404(id) 
            db.session.delete(manager) 
            db.session.commit() 
            return redirect(url_for("index"))

        @app.route('/search')
        @login_required
        def search():
            search = request.args.get('search')
            search_employee=[]
            search_manager=[]
            if search:
                if search.startswith("NV"):
                    search_employee = NhanVien.query.filter(NhanVien.id.ilike(f'%{search}%')).all()
                elif search.startswith("QL"):
                    search_manager = QuanLy.query.filter(QuanLy.id.ilike(f'%{search}%')).all()
                else:
                    return redirect(url_for('index'))
            return render_template('index.html', search_employee=search_employee, search_manager=search_manager, user=current_user)

        @self.web.route("/thongtin")
        @login_required
        def thongtin():
            return render_template("thongtin.html", user=current_user)
        
    def run(self):
        self.web.run(debug=True)

if __name__ == "__main__":
    web = Website()
    web.run()