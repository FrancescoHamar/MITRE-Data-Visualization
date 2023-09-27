import JsonLocalAccess as Jla
import DataAccessPoint as Dap


# Update local relations files by querying the enterprise domain
# Limit is the number of records to save locally
def update_enterprise(limit):
    source = Dap.DataAccessPoint("enterprise_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), limit)
    Jla.access_mit_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), limit)
    Jla.access_tech_mit_e(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), limit)
    Jla.access_comp_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), limit)
    Jla.access_tech_comp_e(True, data=key_vals)


# Update local relations files by querying the mobile domain
# Limit is the number of records to save locally
def update_mobile(limit):
    source = Dap.DataAccessPoint("mobile_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), limit)
    Jla.access_mit_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), limit)
    Jla.access_tech_mit_m(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), limit)
    Jla.access_comp_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), limit)
    Jla.access_tech_comp_m(True, data=key_vals)


# Update local relations files by querying the ics domain
# Limit is the number of records to save locally
def update_ics(limit):
    source = Dap.DataAccessPoint("ics_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), limit)
    Jla.access_mit_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), limit)
    Jla.access_tech_mit_i(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), limit)
    Jla.access_comp_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), limit)
    Jla.access_tech_comp_i(True, data=key_vals)


# Update local phase files by querying the enterprise domain
def update_phase_enterprise():
    source = Dap.DataAccessPoint("enterprise_attack")
    tech, mit, source = source.get_technique_phase()
    Jla.update_phases('e', tech, mit, source)


# Update local phase files by querying the mobile domain
def update_phase_mobile():
    source = Dap.DataAccessPoint("mobile_attack")
    tech, mit, source = source.get_technique_phase()
    Jla.update_phases('m', tech, mit, source)


# Update local phase files by querying the ics domain
def update_phase_ics():
    source = Dap.DataAccessPoint("ics_attack")
    tech, mit, source = source.get_technique_phase()
    Jla.update_phases('i', tech, mit, source)
