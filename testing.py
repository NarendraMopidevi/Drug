# testing get_target_details_from_chembl from chemb_services

from app.services.chembl_services import get_target_details_from_chembl
res1 = get_target_details_from_chembl("CHEMBL2949") #CHEMBL2949,CHEMBL2094253,CHEMBL375
# print(res1)

# testing get_adverse_effect_research_from_pubmed from pubmed_services

from app.services.pubmed_services import get_adverse_effect_research_from_pubmed

res2 = get_adverse_effect_research_from_pubmed("metformin")
print(res2)