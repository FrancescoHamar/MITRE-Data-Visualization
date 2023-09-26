import JsonLocalAccess as Jla
import DataAccessPoint as Dap


def update_enterprise():
    source = Dap.DataAccessPoint("enterprise_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_e(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_e(True, data=key_vals)


def update_mobile():
    source = Dap.DataAccessPoint("mobile_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_m(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_m(True, data=key_vals)


def update_ics():
    source = Dap.DataAccessPoint("ics_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_i(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_i(True, data=key_vals)


def update_phase_enterprise():
    source = Dap.DataAccessPoint("enterprise_attack")
    key_vals = source.get_technique_phase()
    Jla.update_phases('e', key_vals)


def update_phase_mobile():
    source = Dap.DataAccessPoint("mobile_attack")
    key_vals = source.get_technique_phase()
    Jla.update_phases('m', key_vals)


def update_phase_ics():
    source = Dap.DataAccessPoint("ics_attack")
    key_vals = source.get_technique_phase()
    Jla.update_phases('i', key_vals)
