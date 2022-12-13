import streamlit as st
import xml.etree.ElementTree as ET
import xmlschema
import numpy as np

st.set_page_config(layout="wide")
# st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

st.title('JSON to XML Parsing Application')

import pandas as pd
from datetime import datetime as dt
import uuid

col3,col4,col5 = st.columns([1,1,2])

bookfile = col3.file_uploader("Choose a json file for book data")
xsd_file = col3.file_uploader("Choose an XSD File")

if bookfile is not None:
    csdf = pd.read_json(bookfile,typ='series')
    
    # csdf1 = pd.DataFrame([csdf1])
    with col4:
        csdf1 = pd.DataFrame([csdf])
        csdf1 = csdf1.transpose()
        csdf1.reset_index(inplace=True)
        csdf1.columns  =['Key','Value']
        record = csdf1.to_json()
        keycolumn = (csdf1['Key'])
        valuecolumn = (csdf1['Value'])
        csdf1.reset_index(inplace=True)
        # csdf1
    # print(csdf1)
        keyarray = keycolumn.to_numpy()
        valuearray = valuecolumn.to_numpy()
        for index, row in csdf1.iterrows():
            # print(row)
            valuename = row['Value']
            keyname = row['Key']
            jsonvalues = csdf1.iloc[index].to_json()
            st.json(jsonvalues)
            keyname1 = col4.radio(
                    "Is the data for " + keyname +  " field correct",
                    ('Yes', 'No'), key = index
                    )
            if keyname1 == 'No':
                questionfield = col4.text_input('Manual override for ' + row)
                csdf1.at[index,'Value']= questionfield
            elif keyname1 == 'Yes':
                keycolumn = (csdf1['Key'])
                valuecolumn = (csdf1['Value'])
                keyarray = keycolumn.to_numpy()
                valuearray = valuecolumn.to_numpy()
                for record in keyarray:
                    if record == 'book_id':
                        positionofkey = np.where(keyarray == 'book_id')

                #             # print('here' + str(positionofkey))
                        bookid = valuearray[positionofkey]
                        bookid = ' '.join([str(elem) for elem in bookid])
                    if record == 'author':
                        positionofkey = np.where(keyarray == 'author')

                #             # print('here' + str(positionofkey))
                        author = valuearray[positionofkey]
                        author = ' '.join([str(elem) for elem in author])
                    if record == 'title':
                        positionofkey = np.where(keyarray == 'title')

                #             # print('here' + str(positionofkey))
                        title = valuearray[positionofkey]
                        title = ' '.join([str(elem) for elem in title])
                    if record == 'genre':
                        positionofkey = np.where(keyarray == 'genre')

                #             # print('here' + str(positionofkey))
                        genre1 = valuearray[positionofkey]
                        genre1 = ' '.join([str(elem) for elem in genre1])
                    if record == 'price':
                        positionofkey = np.where(keyarray == 'price')

                #             # print('here' + str(positionofkey))
                        floatprice = valuearray[positionofkey]
                        floatprice = ' '.join([str(elem) for elem in floatprice])
                        floatprice = str(floatprice)
                    if record == 'pub_date':
                        positionofkey = np.where(keyarray == 'pub_date')

                #             # print('here' + str(positionofkey))
                        pubdate = valuearray[positionofkey]
                        pubdate = ' '.join([str(elem) for elem in pubdate])
                    if record == 'review':
                        positionofkey = np.where(keyarray == 'review')

                #             # print('here' + str(positionofkey))
                        review = valuearray[positionofkey]
                        review = ' '.join([str(elem) for elem in review])
                    if record == 'availability':
                        positionofkey = np.where(keyarray == 'availability')

                #             # print('here' + str(positionofkey))
                        avail = valuearray[positionofkey]
                        avail = ' '.join([str(elem) for elem in avail])
    with col5:
        # csdf1
        books = ET.Element('bookspackage')
        books.set('xmlns:xsd','http://www.w3.org/2001/XMLSchema')
        bookpackage = ET.SubElement(books, 'books')

        book1 = ET.SubElement(bookpackage, 'book')
        book1.set("id",bookid )
    # 
        bookauthor = ET.SubElement(book1, 'author')
        bookauthor.text = author

        booktitle = ET.SubElement(book1, 'title')
        booktitle.text = title

        bookgenre = ET.SubElement(book1, 'genre')
        bookgenre.text = genre1

        bookprice = ET.SubElement(book1, 'price')
        bookprice.text = floatprice

        bookpubdate = ET.SubElement(book1, 'pub_date')
        pubdate1 = dt.strptime(pubdate,"%m/%d/%Y")
        pubdate1 = pubdate1.strftime("%Y-%m-%d")
        bookpubdate.text = pubdate1

        bookreview = ET.SubElement(book1, 'review')
        # print(review)
        bookreview.text = review

        bookavail = ET.SubElement(book1, 'review')
        # print(review)
        # print(avail)
        if avail == 'False':
            avail = "N/A"
        if avail == 'True':
            avail = "In Stock"
        bookavail.text = avail


        top1 = ET.ElementTree(books)
        treeelement = top1.getroot()
        xml_str = ET.tostring(treeelement, encoding='unicode')
        col5.write(xml_str)
        filename = 'books' + '.xml'

        with open(filename, "w") as f:
            data1 = f.write(xml_str)
            binary = format(data1, 'b')
            
            if xmlschema.validate(xml_str, xsd_file):
                st.error('Error with XML')
            #     # btn = textpreviewcolumn.download_button('Download XML', xml_str, filename)
            else:
                btn = col5.download_button('Download XML', xml_str, filename)
      