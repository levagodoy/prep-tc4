import numpy as np
import streamlit as st

#الحقيقة أبداً لا تموت

def sim_muestra(pesos: np.array, n_dados: int, n_muestras: int):
    """
    Retorna la media de la simulación
    """

    prob = pesos / pesos.sum() #prob normalizada
    muestra = np.arange(1, 7) # array de 1 a 6

    resultado = np.random.choice(muestra, size=(n_muestras, n_dados), p=prob)
    return resultado.mean(axis = 1)

def stat_poblacion(pesos: np.array):
    """
    retorna los valores teoricos de nuestra problacion
    """

    prob = pesos / pesos.sum()
    muestra = np.arange(1, 7)

    mu = np.sum(prob * muestra) #media
    var = np.sum((muestra - mu)**2 * prob) #var

    return mu, var

def sacar_prob(pesos: np.array):
    probs = pesos / pesos.sum()

    return probs


def add_footer():
    footer = """
        <style>
            .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; font-size: 14px; color: #888; }
        </style>
        <div class="footer">
            <p>© 2026 Tomás Leva - SOL512. Todos los derechos reservados.</p>
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)


def render_prob_sliders(key_prefix: str) -> np.array:
    # Initialize session state for these keys if not exists
    for i in range(1, 7):
        key = f"{key_prefix}_w{i}"
        if key not in st.session_state:
            st.session_state[key] = 1.0 / 6.0
    
    # Callback to maintain sum = 1
    def update_probs(changed_index):
        changed_key = f"{key_prefix}_w{changed_index}"
        new_val = st.session_state[changed_key]
        
        # calculate sum of others
        other_keys = [f"{key_prefix}_w{j}" for j in range(1, 7) if j != changed_index]
        sum_others = sum([st.session_state[k] for k in other_keys])
        
        if sum_others == 0:
            # If all others are 0, distribute equally
            for k in other_keys:
                st.session_state[k] = (1.0 - new_val) / 5.0
        else:
            # Scale proportionally
            scale = (1.0 - new_val) / sum_others
            for k in other_keys:
                st.session_state[k] *= scale
                
    pesos = []
    for i in range(1, 7):
        val = st.sidebar.slider(
            f"Probabilidad de Cara {i}", 
            min_value=0.0, 
            max_value=1.0, 
            value=float(st.session_state[f"{key_prefix}_w{i}"]),
            step=0.01,
            key=f"{key_prefix}_w{i}",
            on_change=update_probs,
            args=(i,)
        )
        pesos.append(val)
        
    pesos = np.array(pesos)
    # just to avoid floating point display issues if needed
    if pesos.sum() > 0:
        pesos = pesos / pesos.sum()
    else:
        pesos = np.ones(6) / 6.0
    return pesos
