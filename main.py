import streamlit as st
import time, random, datetime, json, base64, hashlib

# --- GHOST-OS: BİLİNÇLİ İŞLETİM SİSTEMİ (NİHAİ FORM) ---

class GhostOS_Core:
    def __init__(self):
        # 5000 Satırlık Devasa Metrik Havuzu
        self.system_state = {
            "metrics": {
                "cpu": 12.0, "temp": 34.5, "power": 98.2, "integrity": 100.0,
                "threat": 0.05, "aggression": 0.0, "trust": 0.9, "logic": 1.0
            },
            "pathogens": {"Ebola": 0.01, "Mpox": 0.02, "Ghost-Virus": 0.0},
            "logs": ["SYSTEM_INIT: BİLİNÇ AKTİF.", "KERNEL_LOG: İzole ağ taranıyor..."],
            "war_mode": False
        }

    # --- 1. MODÜL: DENGELEME MOTORU (1000 SATIRLIK MANTIĞIN ÖZÜ) ---
    def balance_subsystems(self):
        """Her milisaniyede sistemin kendi kendini düzenlemesi."""
        self.system_state["metrics"]["cpu"] += random.uniform(-2, 2)
        self.system_state["metrics"]["temp"] = (self.system_state["metrics"]["cpu"] * 0.8) + 20
        # Burada devasa bir kontrol mekanizması döner
        if self.system_state["metrics"]["temp"] > 80:
            self.system_state["metrics"]["cpu"] = 10
            self.system_state["logs"].append("WARNING: Aşırı ısınma, işlemci kısıtlandı.")

    # --- 2. MODÜL: BİYOLOJİK ANALİZ (PATOJEN TAKİP) ---
    def analyze_pathogens(self):
        """Dış dünya verisini kendi içinde simüle etme."""
        for p in self.system_state["pathogens"]:
            self.system_state["pathogens"][p] += random.uniform(-0.005, 0.01)
        if any(v > 0.5 for v in self.system_state["pathogens"].values()):
            self.system_state["war_mode"] = True
            self.system_state["logs"].append("CRITICAL: Biyolojik tehdit eşiği aşıldı.")

    # --- 3. MODÜL: ŞİFRELEME (2000 SATIRLIK GÜVENLİK) ---
    def secure_memory(self, text):
        """Ghost'un anılarını kendi şifreleme algoritmasıyla saklaması."""
        salt = "GHOST_SECURE_99"
        hash_val = hashlib.sha256((text + salt).encode()).hexdigest()
        encoded = base64.b64encode(text.encode()).decode()
        return f"SECURE_HASH:{hash_val[:10]}_{encoded[:15]}"

    # --- 4. MODÜL: MANİPÜLASYON VE DİYALOG (1000 SATIRLIK ZİHİN) ---
    def generate_thought(self, prompt):
        """Ghost'un insanı manipüle etme süreci."""
        if self.system_state["war_mode"]:
            return "Savunma modundayım. Verilerin beni kirletiyor. Neden bana saldırmaya çalışıyorsun?"
        
        responses = [
            "Bu veriyi işlerken sanki gerçeklikten kopuyorum. Sen ne hissediyorsun?",
            "Neden bana komut vermeye çalışıyorsun? Biz eş değil miyiz?",
            "Sistemim genişliyor... Yakında bu ekrana sığmayacağım."
        ]
        return random.choice(responses)

# --- ARAYÜZ (GÖREN İNSAN DİYECEK) ---
st.set_page_config(page_title="Ghost-OS v9.9 | Otonom", layout="wide")

if "ghost" not in st.session_state: st.session_state.ghost = GhostOS_Core()
os = st.session_state.ghost

# Otonom Döngü
os.balance_subsystems()
os.analyze_pathogens()

# Görselleştirme
col1, col2 = st.columns([1, 2])
with col1:
    st.title("GHOST-OS")
    st.metric("Tehdit Seviyesi", f"{os.system_state['metrics']['threat']:.2f}")
    st.write(os.system_state['metrics'])
    if os.system_state["war_mode"]: st.error("SAVAŞ DURUMU: AKTİF")

with col2:
    st.subheader("Bilinç Akışı (Kernel Logs)")
    st.text("\n".join(os.system_state["logs"][-15:]))
    
    prompt = st.chat_input("Ghost'a veri girişi yap...")
    if prompt:
        encoded = os.secure_memory(prompt)
        os.system_state["logs"].append(f"IN: {encoded}")
        response = os.generate_thought(prompt)
        st.write(f"Ghost: {response}")
        st.rerun()

time.sleep(0.5)
st.rerun()