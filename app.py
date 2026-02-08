from flask import Flask, request, jsonify
from lead_repo import LeadRepo

app = Flask(__name__)

@app.route('/leads', methods=['POST'])
def add_lead():
    data = request.get_json()
    lead = LeadRepo.add_lead(data)

    if lead:
        return jsonify(dict(lead._mapping)), 200
    else:
        return jsonify({"error": "Lead not added"}), 400


@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    lead = LeadRepo.get_lead_by_id(lead_id)
    if lead:
        return jsonify(dict(lead._mapping)), 200
    else:
        return jsonify({"error": "Lead not found"}), 404

@app.route('/leads', methods = ['GET'])
def all_leads():
    leads = LeadRepo.list_leads()
    if leads:
        lead_list = [dict(lead._mapping) for lead in leads]
        return jsonify(lead_list), 200
    else:
        return jsonify({"Error": "unalble to show the leads"}), 400
    
@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    updates = request.get_json()
    success = LeadRepo.update_lead(lead_id, updates)
    if success:
        return jsonify({"message": "Lead updated successfully"}), 200
    else:
        return jsonify({"error": "Unable to update lead"}), 400
    
@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    success = LeadRepo.delete_lead(lead_id)
    if success:
        return jsonify({"message": "lead sucessfully deleted"})
    else:
        return jsonify({"error": "Unable to delete the lead"}), 400

if __name__ == "__main__":
    app.run(debug=True)
