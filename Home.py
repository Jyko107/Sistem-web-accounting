import streamlit as st
from PIL import Image

# Dummy credentials for simplicity
user = "admin"
passw = "admin"

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def login():
    st.title("Halaman Login")
    st.subheader("Silahkan Untuk Login Terlebih Dahulu")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == user and password == passw:
            st.session_state["logged_in"] = True
            st.sidebar.success("Login berhasil!")
        else:
            st.sidebar.error("Username atau password salah.")            

if not st.session_state["logged_in"]:
    login()

if not st.session_state["logged_in"]:
    st.error("Anda harus login terlebih dahulu.")
else:
    st.sidebar.success("Pilih Menu Diatas ini.")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
    
    with st.container():
        st.subheader("Selamat datang di SITOMB :wave:")
        st.title("Sistem Informasi Soto Bogor - SITOMB")
        st.write('''''')
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Informasi Produk")
            st.write("##")
            st.write("""
                Kami menjual soto mie bogor yang merupakan salah satu makanan khas Nusantara yang terbilang
                soto lengkap karena terdapat banyak bahan-bahan yang disajikan dalam satu mangkoknya.
                Hal unik yang kami sediakan dari makanan berkuah ini adalah penyajiannya yang dilengkapi
                dengan mi kuning, dan risol umumnya soto disajikan hanya menggunakan mi soun atau bihun.
            """)
    
    try:
        Image1 = Image.open('images/sotodag.jpeg')
        Image2 = Image.open('images/soyam.jpeg')
    except FileNotFoundError:
        st.error("Gambar tidak ditemukan, pastikan file gambar berada pada folder yang benar.")
        Image1 = None
        Image2 = None

    with st.container():
        st.write("---")
        st.header("Produk")
        st.write('##')
        left_column, right_column = st.columns(2)
        if Image1:
            with left_column:
                st.image(Image1, caption="Soto Mie Bogor Daging", width=500)
                st.write('##')
                st.write(''' 
                    Soto Bogor Daging yang terbuat dari bahan-bahan
                    Mie Basah, Bihun, Kol, Daging Sapi, Tomat, Bumbu Paon,
                    Bawang Goreng, Daun Daunan.
                ''')
        if Image2:
            with right_column:
                st.image(Image2, caption="Soto Mie Bogor Ayam", width=425)
                st.write('##')
                st.write(''' 
                    Soto Bogor Ayam yang terbuat dari bahan-bahan
                    Mie Basah, Bihun, Kol, Daging Ayam, Tomat, Bumbu Paon,
                    Bawang Goreng, Daun Daunan.
                ''')
        st.write("##")
        st.write("---")

# Assuming make_sidebar() is defined in the navigation module
try:
    from navigation import make_sidebar
    make_sidebar()
except ImportError:
    st.sidebar.error("Modul navigation tidak ditemukan atau make_sidebar() tidak terdefinisi.")
