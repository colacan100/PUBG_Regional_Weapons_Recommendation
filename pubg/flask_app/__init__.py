from flask import Flask
from flask import Flask, render_template 
from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pubg_web.html")

sup_item_ids = ['WeapACE32_C', 'WeapAK47_C', 'WeapAUG_C', 'WeapAWM_C', 'WeapBerreta686_C', 'WeapBerylM762_C', 'WeapBizonPP19_C', 'WeapCowbarProjectile_C', 'WeapCowbar_C', 'WeapCrossbow_1_C', 'WeapDP12_C', 'WeapDP28_C', 'WeapDesertEagle_C', 'WeapFNFal_C', 'WeapG18_C', 'WeapGroza_C', 'WeapHK416_C', 'WeapKar98k_C', 'WeapM16A4_C', 'WeapM1911_C', 'WeapM249_C', 'WeapM24_C', 'WeapM9_C', 'WeapMG3_C', 'WeapMacheteProjectile_C', 'WeapMachete_C', 'WeapMini14_C', 'WeapMk12_C', 'WeapMk14_C', 'WeapMk47Mutant_C', 'WeapNagantM1895_C', 'WeapP90_C', 'WeapPanProjectile_C', 'WeapPan_C', 'WeapQBZ95_C', 'WeapSCAR-L_C', 'WeapSKS_C', 'WeapSaiga12_C', 'WeapSickleProjectile_C', 'WeapSickle_C', 'WeapThompson_C', 'WeapUMP_C', 'WeapUZI_C', 'WeapVSS_C', 'WeapVector_C', 'WeapWinchester_C', 'Weapvz61Skorpion_C']
no_sup_item_ids = ['WeapAK47_C', 'WeapBerreta686_C', 'WeapBerylM762_C', 'WeapBizonPP19_C','WeapCrossbow_1_C', 'WeapDP12_C', 'WeapDP28_C', 'WeapDesertEagle_C', 'WeapFNFal_C', 'WeapG18_C', 'WeapHK416_C', 'WeapKar98k_C', 'WeapM16A4_C', 'WeapM1911_C', 'WeapM24_C', 'WeapM9_C', 'WeapMini14_C', 'WeapMk12_C', 'WeapMk47Mutant_C','WeapNagantM1895_C','WeapQBZ95_C', 'WeapSCAR-L_C', 'WeapSKS_C', 'WeapSaiga12_C', 'WeapThompson_C', 'WeapUMP_C', 'WeapUZI_C', 'WeapVSS_C', 'WeapVector_C', 'WeapWinchester_C', 'Weapvz61Skorpion_C']

with open('../model_erangel.pkl','rb') as pickle_file:
    model_e = pickle.load(pickle_file)

with open('../model_miramar.pkl','rb') as pickle_file:
    model_m = pickle.load(pickle_file)

with open('../model_teigo.pkl','rb') as pickle_file:
    model_t = pickle.load(pickle_file)


def for_recommend(ml_zone,ml_weapons,model):
    zone = ml_zone # 선택지역
    actual_rating = 0
    a = 95
    for ml_weapon in ml_weapons :
        result = model.predict(zone, ml_weapon, actual_rating)
        if result.est < a:
            weapon_result = result
            a = result.est
    return weapon_result.iid

def out_c(name):
    return name[:-2]

def out_weap(name):
    return name[4:-2]
@app.route('/erangel/<zone>',methods=['GET'])
def erangel(zone):
    e = for_recommend(zone,no_sup_item_ids,model_e)
    return render_template('pubg_web2.html', title = e,title_weapon = out_c(e),name_weapon = '추천무기는 ' + out_weap(e) + ' 입니다.')

@app.route('/miramar/<zone>',methods=['GET'])
def miramar(zone):
    m = for_recommend(zone,no_sup_item_ids,model_m)
    return render_template('pubg_web2.html', title = m,title_weapon = out_c(m),name_weapon = '추천무기는 ' + out_weap(m) + ' 입니다.')

@app.route('/teigo/<zone>',methods=['GET'])
def teigo(zone):
    t = for_recommend(zone,no_sup_item_ids,model_t)
    return render_template('pubg_web2.html', title = t,title_weapon = out_c(t),name_weapon = '추천무기는 ' + out_weap(t) + ' 입니다.')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)