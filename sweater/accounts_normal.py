from flask import render_template, request, session
from flask_login import login_required

from sweater import app
from sweater.models import Customer, Done_accounts
from sweater.forms import Acounts


@app.route('/accounts_normal', methods=['GET', 'POST'])
@login_required
def accounts_normal():
    form = Acounts()
    client_id = session.get('id_client', None)
    client = Customer.query.get(client_id)
    val7 = client.rate
    accounts = Done_accounts.query.filter_by(client_id=client_id)
    if request.method == "POST":
        val1 = form.model.data
        val2 = float(request.form["consumption"])
        val3 = float(request.form["number_of_cars"])
        val4 = float(request.form["start_of_placement"])
        val5 = float(request.form["end_of_placement"])
        val6 = float(request.form["simple_in_hours"])
        val8 = float(((val5 - val4) + 1) - (val6 / 24))
        result = round(float((((val2 * val3) * float(val7)) * val8) * 24), 3)

        if request.form.get("add"):

            session['id_client_db'] = client_id
            session['model'] = int(val1)
            session['consumption'] = val2
            session['number_of_cars'] = val3
            session['start_of_placement'] = val4
            session['end_of_placement'] = val5
            session['simple_in_hours'] = val6
            session['result_day'] = round(val8, 3)
            session['result'] = result

        return render_template('accounts_normal.html',
                               client=client, accounts=accounts, client_id=client_id, form=form, val=result)

    return render_template('accounts_normal.html',
                           client_id=client_id, client=client, accounts=accounts, form=form)
