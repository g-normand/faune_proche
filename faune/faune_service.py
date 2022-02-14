import datetime


def get_gps_from_google_maps(url):
    url_split = url.split('/')
    for split in url_split:
        if split.startswith('@'):
            lat_long = split[1:].split('?')[0].split(',')
            latitude = round(float(lat_long[0]), 2)
            longitude = round(float(lat_long[1]), 2)
    return latitude, longitude


def get_infos_from_url(url, pas):
    pas = float(pas)
    latitude, longitude = get_gps_from_google_maps(url)

    today = datetime.date.today()
    six_months_ago = today - datetime.timedelta(days=6* 30)

    url = "https://www.faune-france.org/index.php?m_id=94&&p_c=3&p_cc=-1&sp_tg=3&sp_DateSynth=%(end)s&sp_DChoice=range&sp_DFrom=%(start)s&sp_DTo=%(end)s&sp_DCa=0&sp_SChoice=all&sp_PChoice=coord&sp_Coord[N]=%(max_lat)s&sp_Coord[W]=%(min_lon)s&sp_Coord[S]=%(min_lat)s&sp_Coord[E]=%(max_lon)s&sp_FChoice=list&sp_FGraphFormat=auto&sp_FMapFormat=none&sp_FDisplay=DATE_PLACE_SPECIES&sp_FOrder=ALPHA&sp_FOrderListSpecies=ALPHA&sp_FListSpeciesChoice=DATA&sp_FOrderSynth=ALPHA&sp_FGraphChoice=DATA&sp_DFormat=DESC&sp_FAltScale=250&sp_FAltChoice=DATA&sp_FExportFormat=XLS&sp_tg=1"
    infos_dict = {}
    infos_dict['start'] = six_months_ago.strftime('%d.%m.%y')
    infos_dict['end'] = today.strftime('%d.%m.%y')
    infos_dict['min_lat'] = latitude - pas
    infos_dict['max_lat'] = latitude + pas
    infos_dict['min_lon'] = longitude - pas
    infos_dict['max_lon'] = longitude + pas

    return url % infos_dict


def get_place(url):
    url_split = url.split('/')
    return url_split[5]
