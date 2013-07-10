
<%inherit file="base.mako"/>

<%block name = "content">
    <div class="main_box_left">
        <div class="name_product">
            Product name: ${product_name}
            <p style = "margin-top:15px"><a href = "${'#' if allegro_link is None else allegro_link}"> ${allegro_link} </a></p>
            <p style = "margin-top:15px"><a href = "${'#' if allegro_link is None else allegro_link}"> ${nokaut_link} </a></p>
        </div>
        <div class="box_photo">
            <p style="margin-top:250px"> <br></p>
       <!--     <img src="${request.static_url('pyramid_app:static/img/img_demo.jpg')}" alt="img_demo"/>-->
        </div>
    </div>
    <div class="main_box_right">
        <div class="compare_box">
            <img src="${request.static_url('pyramid_app:static/img/logo_allegro.png')}" alt="logo_allegro"/>
            <div class="${'price '+ allegro_price_mode}">${allegro_price}</div>
        </div>
        <div class="compare_box">
            <img src="${request.static_url('pyramid_app:static/img/logo_nokaut.png')}" alt="logo_nokaut"/>
            <div class="${'price '+ nokaut_price_mode}">${nokaut_price}</div>
        </div>
    </div>
</%block>