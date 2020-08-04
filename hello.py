import urllib.request


def  download_files():
    id=['113865','113886','113905','113925','198755','198755']

    for i in range(5):
        url='https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_' \
            'lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&' \
            '_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ' \
            '_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID='+id[i]+'&_documents_WAR_publicationsportlet_INSTANCE_' \
            'VBZOni0vs5VJ_locale=en'
        urllib.request.urlretrieve(url ,'text201'+str(i+1)+'.xls')
