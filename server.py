from sanic import Sanic
from sanic import response
from sanic.response import html
from sanic.response import json

app = Sanic('MeuApp')

# Inicio da aplicação
@app.route('/')
async def index(request):
    return await response.file_stream('index.html')

# Página de propriedades
@app.route('/property')
async def prop(request):
    return await response.file_stream('property.html')

# Página de agentes
@app.route('/agents')
async def agents(request):
    return await response.file_stream('about-us.html')

# Página de blog
@app.route('/news')
async def news(request):
    return await response.file_stream('blog.html')

# Página de 'pages'
@app.route('/pages')
async def pages(request):
    return await response.file_stream('property-details.html')

# Página de contato
@app.route('/contact')
async def contact(request):
    return await response.file_stream('contact.html')

"""
# Styles da Página
"""

# Pasta com style.css
@app.route('/css/style.css')
async def style(request):
    return await response.file_stream('css/style.css')

# Pasta com icons
@app.route('/css/bootstrap.min.css')
async def bootstrap_min_css(request):
    return await response.file_stream('css/bootstrap.min.css')

# Pasta com icons
@app.route('/css/elegant-icons.css')
async def elegant_icons(request):
    return await response.file_stream('css/elegant-icons.css')

# Pasta com icons
@app.route('/css/themify-icons.css')
async def themify_icons(request):
    return await response.file_stream('css/themify-icons.css')

# Pasta com font-awesome.min.css
@app.route('/css/font-awesome.min.css')
async def font_awesome_min_css(request):
    return await response.file_stream('css/font-awesome.min.css')

# Pasta com nice-select.css
@app.route('/css/nice-select.css')
async def nice_select_css(request):
    return await response.file_stream('css/nice-select.css')

# Pasta com jquery-ui.min.css
@app.route('/css/jquery-ui.min.css')
async def jquery_ui_min_css(request):
    return await response.file_stream('css/jquery-ui.min.css')

# Pasta com owl.carousel.min.css
@app.route('/css/owl.carousel.min.css')
async def owl_carousel_min_css(request):
    return await response.file_stream('css/owl.carousel.min.css')

# Pasta com slicknav
@app.route('/css/slicknav.min.css')
async def slicknav_min_css(request):
    return await response.file_stream('css/slicknav.min.css')

# Pasta com magnific-popup.css
@app.route('/css/magnific-popup.css')
async def magnific_popup_css(request):
    return await response.file_stream('css/magnific-popup.css')

"""
# Js da Página
"""

# Pasta com bootstrap js
@app.route('/js/bootstrap.min.js')
async def bootstrap_min_js(request):
    return await response.file_stream('js/bootstrap.min.js')

# Pasta com bootstrap.min.js.map js
@app.route('/js/bootstrap.min.js.map')
async def bootstrap_min_js_map(request):
    return await response.file_stream('js/bootstrap.min.js.map')

# Pasta com jquery-3.3.1.min.js
@app.route('/js/jquery-3.3.1.min.js')
async def jquery_3_3_1_min_js(request):
    return await response.file_stream('js/jquery-3.3.1.min.js')

# Pasta com jquery.magnific-popup.min.js js
@app.route('/js/jquery.magnific-popup.min.js')
async def jquery_magnific_popup_min_js(request):
    return await response.file_stream('js/jquery.magnific-popup.min.js')

# Pasta com jquery.nice-select.min.js js
@app.route('/js/jquery.nice-select.min.js')
async def jquery_nice_select_min_js(request):
    return await response.file_stream('js/jquery.nice-select.min.js')

# Pasta com jquery.slicknav.js js
@app.route('/js/jquery.slicknav.js')
async def jquery_slicknav_js(request):
    return await response.file_stream('js/jquery.slicknav.js')

# Pasta com jquery-ui.min.js js
@app.route('/js/jquery-ui.min.js')
async def jquery_ui_min_js(request):
    return await response.file_stream('js/jquery-ui.min.js')

# Pasta com owl.carousel.min.js js
@app.route('/js/owl.carousel.min.js')
async def owl_carousel_min_js(request):
    return await response.file_stream('js/owl.carousel.min.js')

# Pasta com main.js
@app.route('/js/main.js')
async def main_js(request):
    return await response.file_stream('js/main.js')

"""
# Img's da Página
"""

"""
# Pasta com os agentes
"""

# Pasta com agent-1.jpg
@app.route('/img/agent/agent-1.jpg')
async def agent_1_jpg(request):
    return await response.file_stream('img/agent/agent-1.jpg')

# Pasta com agent-2.jpg
@app.route('/img/agent/agent-2.jpg')
async def agent_2_jpg(request):
    return await response.file_stream('img/agent/agent-2.jpg')

# Pasta com agent-3.jpg
@app.route('/img/agent/agent-3.jpg')
async def agent_3_jpg(request):
    return await response.file_stream('img/agent/agent-3.jpg')

# Pasta com agent-4.jpg
@app.route('/img/agent/agent-4.jpg')
async def agent_4_jpg(request):
    return await response.file_stream('img/agent/agent-4.jpg')

# Pasta com agent-5.jpg
@app.route('/img/agent/agent-5.jpg')
async def agent_5_jpg(request):
    return await response.file_stream('img/agent/agent-5.jpg')

"""
# Pasta com o blog comment
"""

# Pasta com comment-1.jpg
@app.route('/img/blog/comment/comment-1.jpg')
async def comment_1_jpg(request):
    return await response.file_stream('img/blog/comment/comment-1.jpg')

# Pasta com comment-2.jpg
@app.route('/img/blog/comment/comment-2.jpg')
async def comment_2_jpg(request):
    return await response.file_stream('img/blog/comment/comment-2.jpg')

# Pasta com comment-3.jpg
@app.route('/img/blog/comment/comment-3.jpg')
async def comment_3_jpg(request):
    return await response.file_stream('img/blog/comment/comment-3.jpg')

"""
# Pasta com o blog
"""

# Pasta com blog-details-1.jpg
@app.route('/img/blog/blog-details-1.jpg')
async def blog_details_1_jpg(request):
    return await response.file_stream('img/blog/blog-details-1.jpg')

# Pasta com blog-details-2.jpg
@app.route('/img/blog/blog-details-2.jpg')
async def blog_details_2_jpg(request):
    return await response.file_stream('img/blog/blog-details-2.jpg')

# Pasta com blog-details-3.jpg
@app.route('/img/blog/blog-details-3.jpg')
async def blog_details_3_jpg(request):
    return await response.file_stream('img/blog/blog-details-3.jpg')

# Pasta com blog-details-4.jpg
@app.route('/img/blog/blog-details-4.jpg')
async def blog_details_4_jpg(request):
    return await response.file_stream('img/blog/blog-details-4.jpg')

# Pasta com blog-details-also-1.jpg
@app.route('/img/blog/blog-details-also-1.jpg')
async def blog_details_also_1_jpg(request):
    return await response.file_stream('img/blog/blog-details-also-1.jpg')

# Pasta com blog-details-also-2.jpg
@app.route('/img/blog/blog-details-also-2.jpg')
async def blog_details_also_2_jpg(request):
    return await response.file_stream('img/blog/blog-details-also-2.jpg')

# Pasta com blog-details-hero.jpg
@app.route('/img/blog/blog-details-hero.jpg')
async def blog_details_hero_jpg(request):
    return await response.file_stream('img/blog/blog-details-hero.jpg')

# Pasta com latest-1.jpg
@app.route('/img/blog/latest-1.jpg')
async def latest_1_jpg(request):
    return await response.file_stream('img/blog/latest-1.jpg')

# Pasta com latest-2.jpg
@app.route('/img/blog/latest-2.jpg')
async def latest_2_jpg(request):
    return await response.file_stream('img/blog/latest-2.jpg')

# Pasta com latest-3.jpg
@app.route('/img/blog/latest-3.jpg')
async def latest_3_jpg(request):
    return await response.file_stream('img/blog/latest-3.jpg')

# Pasta com latest-4.jpg
@app.route('/img/blog/latest-4.jpg')
async def latest_4_jpg(request):
    return await response.file_stream('img/blog/latest-4.jpg')

# Pasta com latest-5.jpg
@app.route('/img/blog/latest-5.jpg')
async def latest_5_jpg(request):
    return await response.file_stream('img/blog/latest-5.jpg')

# Pasta com latest-6.jpg
@app.route('/img/blog/latest-6.jpg')
async def latest_6_jpg(request):
    return await response.file_stream('img/blog/latest-6.jpg')

# Pasta com latest-7.jpg
@app.route('/img/blog/latest-7.jpg')
async def latest_7_jpg(request):
    return await response.file_stream('img/blog/latest-7.jpg')

# Pasta com latest-8.jpg
@app.route('/img/blog/latest-8.jpg')
async def latest_8_jpg(request):
    return await response.file_stream('img/blog/latest-8.jpg')


"""
# Pasta com as features
"""


# Pasta com f-author-1.jpg
@app.route('/img/feature/f-author-1.jpg')
async def f_author_1_jpg(request):
    return await response.file_stream('img/feature/f-author-1.jpg')

# Pasta com f-author-2.jpg
@app.route('/img/feature/f-author-2.jpg')
async def f_author_2_jpg(request):
    return await response.file_stream('img/feature/f-author-2.jpg')

# Pasta com f-author-3.jpg
@app.route('/img/feature/f-author-3.jpg')
async def f_author_3_jpg(request):
    return await response.file_stream('img/feature/f-author-3.jpg')

# Pasta com feature-1.jpg
@app.route('/img/feature/feature-1.jpg')
async def feature_1_jpg(request):
    return await response.file_stream('img/feature/feature-1.jpg')

# Pasta com feature-2.jpg
@app.route('/img/feature/feature-2.jpg')
async def feature_2_jpg(request):
    return await response.file_stream('img/feature/feature-2.jpg')

# Pasta com feature-3.jpg
@app.route('/img/feature/feature-3.jpg')
async def feature_3_jpg(request):
    return await response.file_stream('img/feature/feature-3.jpg')

# Pasta com feature-4.jpg
@app.route('/img/feature/feature-4.jpg')
async def feature_4_jpg(request):
    return await response.file_stream('img/feature/feature-4.jpg')

# Pasta com feature-5.jpg
@app.route('/img/feature/feature-5.jpg')
async def feature_5_jpg(request):
    return await response.file_stream('img/feature/feature-5.jpg')


"""
# Pasta com hero
"""

# Pasta com dot-1.jpg
@app.route('/img/hero/dot-1.jpg')
async def dot_1_jpg(request):
    return await response.file_stream('img/hero/dot-1.jpg')

# Pasta com dot-2.jpg
@app.route('/img/hero/dot-2.jpg')
async def dot_2_jpg(request):
    return await response.file_stream('img/hero/dot-2.jpg')

# Pasta com dot-3.jpg
@app.route('/img/hero/dot-3.jpg')
async def dot_3_jpg(request):
    return await response.file_stream('img/hero/dot-3.jpg')

# Pasta com hero-1.jpg
@app.route('/img/hero/hero-1.jpg')
async def hero_1_jpg(request):
    return await response.file_stream('img/hero/hero-1.jpg')

# Pasta com hero-2.jpg
@app.route('/img/hero/hero-2.jpg')
async def hero_2_jpg(request):
    return await response.file_stream('img/hero/hero-2.jpg')

# Pasta com hero-3.jpg
@app.route('/img/hero/hero-3.jpg')
async def hero_3_jpg(request):
    return await response.file_stream('img/hero/hero-3.jpg')


"""
# Pasta com howit-works
"""

# Pasta com howit-works-1.png
@app.route('/img/howit-works/howit-works-1.png')
async def howit_works_1_png(request):
    return await response.file_stream('img/howit-works/howit-works-1.png')

# Pasta com howit-works-2.png
@app.route('/img/howit-works/howit-works-2.png')
async def howit_works_2_png(request):
    return await response.file_stream('img/howit-works/howit-works-2.png')

# Pasta com howit-works-3.png
@app.route('/img/howit-works/howit-works-3.png')
async def howit_works_3_png(request):
    return await response.file_stream('img/howit-works/howit-works-3.png')


"""
# Pasta com os partners
"""

# Pasta com partner-1.png
@app.route('/img/partner/partner-1.png')
async def partner_1_png(request):
    return await response.file_stream('img/partner/partner-1.png')

# Pasta com partner-2.png
@app.route('/img/partner/partner-2.png')
async def partner_2_png(request):
    return await response.file_stream('img/partner/partner-2.png')

# Pasta com partner-3.png
@app.route('/img/partner/partner-3.png')
async def partner_3_png(request):
    return await response.file_stream('img/partner/partner-3.png')

# Pasta com partner-4.png
@app.route('/img/partner/partner-4.png')
async def partner_4_png(request):
    return await response.file_stream('img/partner/partner-4.png')

# Pasta com partner-5.png
@app.route('/img/partner/partner-5.png')
async def partner_5_png(request):
    return await response.file_stream('img/partner/partner-5.png')


"""
# Pasta com properties
"""

# Pasta com agent-contact.jpg
@app.route('/img/properties/agent-contact.jpg')
async def agent_contact_jpg(request):
    return await response.file_stream('img/properties/agent-contact.jpg')

# Pasta com best-agent-1.jpg
@app.route('/img/properties/best-agent-1.jpg')
async def best_agent_1_jpg(request):
    return await response.file_stream('img/properties/best-agent-1.jpg')

# Pasta com best-agent-2.jpg
@app.route('/img/properties/best-agent-2.jpg')
async def best_agent_2_jpg(request):
    return await response.file_stream('img/properties/best-agent-2.jpg')

# Pasta com best-agent-3.jpg
@app.route('/img/properties/best-agent-3.jpg')
async def best_agent_3_jpg(request):
    return await response.file_stream('img/properties/best-agent-3.jpg')

# Pasta com product-content-bg.jpg
@app.route('/img/properties/product-content-bg.jpg')
async def product_content_bg_jpg(request):
    return await response.file_stream('img/properties/product-content-bg.jpg')

# Pasta com properties-1.jpg
@app.route('/img/properties/properties-1.jpg')
async def properties_1_jpg(request):
    return await response.file_stream('img/properties/properties-1.jpg')

# Pasta com properties-2.jpg
@app.route('/img/properties/properties-2.jpg')
async def properties_2_jpg(request):
    return await response.file_stream('img/properties/properties-2.jpg')

# Pasta com property-1.jpg
@app.route('/img/properties/property-1.jpg')
async def property_1_jpg(request):
    return await response.file_stream('img/properties/property-1.jpg')

# Pasta com property-2.jpg
@app.route('/img/properties/property-2.jpg')
async def property_2_jpg(request):
    return await response.file_stream('img/properties/property-2.jpg')

# Pasta com property-3.jpg
@app.route('/img/properties/property-3.jpg')
async def property_3_jpg(request):
    return await response.file_stream('img/properties/property-3.jpg')

# Pasta com property-4.jpg
@app.route('/img/properties/property-4.jpg')
async def property_4_jpg(request):
    return await response.file_stream('img/properties/property-4.jpg')

# Pasta com property-details-b1.jpg
@app.route('/img/properties/property-details-b1.jpg')
async def property_details_b1_jpg(request):
    return await response.file_stream('img/properties/property-details-b1.jpg')

# Pasta com property-details-b2.jpg
@app.route('/img/properties/property-details-b2.jpg')
async def property_details_b2_jpg(request):
    return await response.file_stream('img/properties/property-details-b2.jpg')

# Pasta com property-details-b3.jpg
@app.route('/img/properties/property-details-b3.jpg')
async def property_details_b3_jpg(request):
    return await response.file_stream('img/properties/property-details-b3.jpg')

# Pasta com property-details-b4.jpg
@app.route('/img/properties/property-details-b4.jpg')
async def property_details_b4_jpg(request):
    return await response.file_stream('img/properties/property-details-b4.jpg')

# Pasta com property-details-b5.jpg
@app.route('/img/properties/property-details-b5.jpg')
async def property_details_b5_jpg(request):
    return await response.file_stream('img/properties/property-details-b5.jpg')

# Pasta com thumb-1.jpg
@app.route('/img/properties/thumb-1.jpg')
async def thumb_1_jpg(request):
    return await response.file_stream('img/properties/thumb-1.jpg')

# Pasta com thumb-2.jpg
@app.route('/img/properties/thumb-2.jpg')
async def thumb_2_jpg(request):
    return await response.file_stream('img/properties/thumb-2.jpg')

# Pasta com thumb-3.jpg
@app.route('/img/properties/thumb-3.jpg')
async def thumb_3_jpg(request):
    return await response.file_stream('img/properties/thumb-3.jpg')

# Pasta com thumb-4.jpg
@app.route('/img/properties/thumb-4.jpg')
async def thumb_4_jpg(request):
    return await response.file_stream('img/properties/thumb-4.jpg')

# Pasta com thumb-5.jpg
@app.route('/img/properties/thumb-5.jpg')
async def thumb_5_jpg(request):
    return await response.file_stream('img/properties/thumb-5.jpg')

"""
# Pasta de imagens soltas
"""

# flag.png
@app.route('/img/flag.png')
async def flag_png(request):
    return await response.file_stream('img/flag.png')

# footer-bg.jpg
@app.route('/img/footer-bg.jpg')
async def footer_bg_jpg(request):
    return await response.file_stream('img/footer-bg.jpg')

# footer-logo.png
@app.route('/img/footer-logo.png')
async def footer_logo_png(request):
    return await response.file_stream('img/footer-logo.png')

# testimonial-bg.jpg
@app.route('/img/testimonial-bg.jpg')
async def testimonial_bg_jpg(request):
    return await response.file_stream('img/testimonial-bg.jpg')

# video-bg.jpg
@app.route('/img/video-bg.jpg')
async def video_bg_jpg(request):
    return await response.file_stream('img/video-bg.jpg')

# logo.png
@app.route('/img/logo.png')
async def logo_png(request):
    return await response.file_stream('img/logo.png')

"""
# Pasta com Fonts
"""

# Pasta com ElegantIcons.svg
@app.route('/fonts/ElegantIcons.svg')
async def ElegantIcons_svg(request):
    return await response.file_stream('fonts/ElegantIcons.svg')

# Pasta com ElegantIcons.eot
@app.route('/fonts/ElegantIcons.eot')
async def ElegantIcons_eot(request):
    return await response.file_stream('fonts/ElegantIcons.eot')

# Pasta com ElegantIcons.ttf
@app.route('/fonts/ElegantIcons.ttf')
async def ElegantIcons_ttf(request):
    return await response.file_stream('fonts/ElegantIcons.ttf')

# Pasta com ElegantIcons.woff
@app.route('/fonts/ElegantIcons.woff')
async def ElegantIcons_woff(request):
    return await response.file_stream('fonts/ElegantIcons.woff')

# Pasta com fontawesome-webfont.eot
@app.route('/fonts/fontawesome-webfont.eot')
async def fontawesome_webfont_eot(request):
    return await response.file_stream('fonts/fontawesome-webfont.eot')

# Pasta com fontawesome-webfont.svg
@app.route('/fonts/fontawesome-webfont.svg')
async def fontawesome_webfont_svg(request):
    return await response.file_stream('fonts/fontawesome-webfont.svg')

# Pasta com fontawesome-webfont.ttf
@app.route('/fonts/fontawesome-webfont.ttf')
async def fontawesome_webfont_ttf(request):
    return await response.file_stream('fonts/fontawesome-webfont.ttf')

# Pasta com fontawesome-webfont.woff
@app.route('/fonts/fontawesome-webfont.woff')
async def fontawesome_webfont_woff(request):
    return await response.file_stream('fonts/fontawesome-webfont.woff')

# Pasta com fontawesome-webfont.woff2
@app.route('/fonts/fontawesome-webfont.woff2')
async def fontawesome_webfont_woff2(request):
    return await response.file_stream('fonts/fontawesome-webfont.woff2')

# Pasta com FontAwesome.otf
@app.route('/fonts/FontAwesome.otf')
async def FontAwesome_otf(request):
    return await response.file_stream('fonts/FontAwesome.otf')

# Pasta com themify.eot
@app.route('/fonts/themify.eot')
async def themify_eot(request):
    return await response.file_stream('fonts/themify.eot')

# Pasta com themify.svg
@app.route('/fonts/themify.svg')
async def themify_svg(request):
    return await response.file_stream('fonts/themify.svg')

# Pasta com themify.ttf
@app.route('/fonts/themify.ttf')
async def themify_ttf(request):
    return await response.file_stream('fonts/themify.ttf')

# Pasta com themify.woff
@app.route('/fonts/themify.woff')
async def themify_woff(request):
    return await response.file_stream('fonts/themify.woff')


#------------------------------------------------------------------------------------------#


# Gatilho de inicialização
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=False)
