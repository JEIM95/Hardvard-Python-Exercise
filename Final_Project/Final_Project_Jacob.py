import streamlit as st
import pandas as pd
import uuid

class Transaccion:
    def __init__(self, id, fecha, importe, concepto):
        self.id = id
        self.fecha = fecha
        self.importe = importe
        self.concepto = concepto

class Cartilla:
    def __init__(self, id, balance_inicial):
        self.id = id
        self.balance_inicial = balance_inicial
        self.transacciones = []

    def __str__(self):
        return f"Cartilla {self.id} con balance de {self.balance()}"
    
    def balance(self):
        return sum(transaccion.importe for transaccion in self.transacciones) + self.balance_inicial

    def add_income(self, fecha, importe, concepto):
        self.transacciones.append(Transaccion(uuid.uuid4(), fecha, abs(importe), concepto))

    def add_outcome(self, fecha, importe, concepto):
        self.transacciones.append(Transaccion(uuid.uuid4(), fecha, -abs(importe), concepto))

    def get_history(self):
        return self.transacciones
    
if "cartilla" not in st.session_state:  
    st.session_state.cartilla = Cartilla(uuid.uuid4(), 5200)
    st.session_state.cartilla.add_income("2025-01-01", 1000, "Sueldo")
    st.session_state.cartilla.add_outcome("2025-01-02", 150, "Cena")
    st.session_state.cartilla.add_outcome("2025-01-03", 600, "iPhone")
    st.session_state.cartilla.add_outcome("2025-01-04", 82, "Supermercado")

# Custom CSS for styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #4CAF50;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .balance-container {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .balance-amount {
        font-size: 4rem;
        font-weight: bold;
        color: white;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .balance-label {
        font-size: 1.5rem;
        color: rgba(255,255,255,0.9);
        margin-top: 0.5rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .section-header {
        color: #333;
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 25px !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(240, 147, 251, 0.3) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(240, 147, 251, 0.4) !important;
    }
    
    .modern-table {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 20px;
        box-shadow: 
            0 20px 40px rgba(30, 60, 114, 0.3),
            0 0 0 1px rgba(255, 255, 255, 0.1);
        overflow: hidden;
        margin: 2rem 0;
        max-height: 400px;
        overflow-y: auto;
    }
    
    .modern-table::-webkit-scrollbar {
        width: 8px;
    }
    
    .modern-table::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .modern-table::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
    
    .modern-table::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    
    .modern-table table {
        width: 100%;
        border-collapse: collapse;
        background: transparent;
    }
    
    .modern-table th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        padding: 20px;
        text-align: center;
        border: none;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-size: 1.1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        position: sticky;
        top: 0;
        z-index: 10;
    }
    
    .modern-table td {
        padding: 18px 20px;
        text-align: center;
        border: none;
        background: rgba(255, 255, 255, 0.05);
        color: white;
        font-size: 1rem;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .modern-table tr:nth-child(even) td {
        background: rgba(255, 255, 255, 0.08);
    }
    
    .modern-table tr:hover td {
        background: rgba(255, 255, 255, 0.15);
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .positive-amount {
        color: #4ade80;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(74, 222, 128, 0.5);
        background: linear-gradient(135deg, rgba(74, 222, 128, 0.2), rgba(34, 197, 94, 0.1));
        padding: 8px 16px;
        border: 1px solid rgba(74, 222, 128, 0.3);
    }
    
    .negative-amount {
        color: #f87171;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(248, 113, 113, 0.5);
        background: linear-gradient(135deg, rgba(248, 113, 113, 0.2), rgba(239, 68, 68, 0.1));
        padding: 8px 16px;
        border: 1px solid rgba(248, 113, 113, 0.3);
    }
    
    .date-cell {
        color: #a78bfa;
        font-weight: 600;
        text-shadow: 0 0 8px rgba(167, 139, 250, 0.4);
    }
    
    .concept-cell {
        color: #fbbf24;
        font-weight: 500;
        text-shadow: 0 0 8px rgba(251, 191, 36, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="main-title">Bienvenido Josele</h1>', unsafe_allow_html=True)

# Balance section with custom styling
st.markdown(f"""
<div class="balance-container">
    <div class="balance-amount">{st.session_state.cartilla.balance():.2f}€</div>
    <div class="balance-label">Balance</div>
</div>
""", unsafe_allow_html=True)

# Transaction history section
st.markdown('<h2 class="section-header">Historial de transacciones</h2>', unsafe_allow_html=True)

historico = st.session_state.cartilla.get_history()

if historico:
    ids = [transaccion.id for transaccion in historico]
    fechas = [transaccion.fecha for transaccion in historico]
    importes = [f"{transaccion.importe:.2f}€" for transaccion in historico]
    conceptos = [transaccion.concepto for transaccion in historico]
    
    # Create custom HTML table with modern styling
    table_html = '<div class="modern-table"><table>'
    table_html += '<thead><tr><th>Fecha</th><th>Importe</th><th>Concepto</th></tr></thead><tbody>'
    
    for i, (fecha, importe, concepto) in enumerate(zip(fechas, importes, conceptos)):
        # Determine if amount is positive or negative for styling
        amount_class = "positive-amount" if not importe.startswith('-') else "negative-amount"
        table_html += f'<tr><td class="date-cell">{fecha}</td><td class="{amount_class}">{importe}</td><td class="concept-cell">{concepto}</td></tr>'
    
    table_html += '</tbody></table></div>'
    st.markdown(table_html, unsafe_allow_html=True)

# Add transaction section
st.markdown('<h2 class="section-header">Añadir transacción</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    fecha = st.date_input("📅 Fecha")
with col2:
    importe = st.number_input("💰 Importe", step=0.01, format="%.2f")
with col3:
    concepto = st.text_input("📝 Concepto")

if st.button("✨ Añadir Transacción"):
    if importe != 0 and concepto:
        if importe > 0:
            st.session_state.cartilla.add_income(fecha, importe, concepto)
        else:
            st.session_state.cartilla.add_outcome(fecha, importe, concepto)
        st.rerun()
    else:
        st.error("Por favor, introduce un importe válido y un concepto")
