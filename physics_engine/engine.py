"""
Physics Engine
==============
A comprehensive physics formula and simulation engine covering:
- Classical Mechanics (kinematics, dynamics, energy, momentum)
- Thermodynamics (laws, heat, work, entropy, ideal gas)
- Electrostatics and Electrodynamics (Coulomb, fields, circuits)
- Wave Mechanics and Optics
- Special Relativity (time dilation, length contraction, mass-energy)
- Quantum Mechanics basics (Planck, de Broglie, Heisenberg)
- Gravity and Orbital Mechanics
- Fluid Dynamics (Bernoulli, pressure, flow)
"""

from __future__ import annotations
import math
import numpy as np
from typing import Dict, Any, Optional, List, Tuple


# Physical Constants (SI units)
CONSTANTS = {
    "c": 299_792_458,          # Speed of light (m/s)
    "G": 6.674e-11,            # Gravitational constant
    "h": 6.626e-34,            # Planck constant (J·s)
    "hbar": 1.055e-34,         # Reduced Planck constant
    "k_B": 1.381e-23,          # Boltzmann constant (J/K)
    "e": 1.602e-19,            # Elementary charge (C)
    "m_e": 9.109e-31,          # Electron mass (kg)
    "m_p": 1.673e-27,          # Proton mass (kg)
    "N_A": 6.022e23,           # Avogadro constant (mol^-1)
    "R": 8.314,                # Gas constant (J/mol·K)
    "epsilon_0": 8.854e-12,    # Vacuum permittivity
    "mu_0": 1.257e-6,          # Vacuum permeability
    "sigma_SB": 5.671e-8,      # Stefan-Boltzmann constant
    "g": 9.80665               # Standard gravity (m/s²)
}


class PhysicsEngine:
    """Comprehensive physics computation engine."""

    @staticmethod
    def get_constants() -> Dict[str, Any]:
        """Return all physical constants with descriptions."""
        descriptions = {
            "c": "Speed of light in vacuum (m/s)",
            "G": "Gravitational constant (N·m²/kg²)",
            "h": "Planck constant (J·s)",
            "hbar": "Reduced Planck constant ℏ = h/2π (J·s)",
            "k_B": "Boltzmann constant (J/K)",
            "e": "Elementary charge (C)",
            "m_e": "Electron mass (kg)",
            "m_p": "Proton mass (kg)",
            "N_A": "Avogadro constant (mol⁻¹)",
            "R": "Ideal gas constant (J/mol·K)",
            "epsilon_0": "Vacuum permittivity (F/m)",
            "mu_0": "Vacuum permeability (H/m)",
            "sigma_SB": "Stefan-Boltzmann constant (W/m²·K⁴)",
            "g": "Standard gravitational acceleration (m/s²)"
        }
        return {k: {"value": v, "description": descriptions[k]}
                for k, v in CONSTANTS.items()}

    # ──────────────────────────────────────────────
    # Classical Mechanics – Kinematics
    # ──────────────────────────────────────────────

    @staticmethod
    def kinematics_1d(v0: float, a: float, t: float,
                      x0: float = 0.0) -> Dict[str, Any]:
        """
        1D kinematics under constant acceleration.
        v = v0 + at
        x = x0 + v0*t + ½at²
        v² = v0² + 2a(x - x0)
        """
        v = v0 + a * t
        x = x0 + v0 * t + 0.5 * a * t**2
        v_sq = v0**2 + 2 * a * (x - x0)
        return {
            "initial_velocity": v0,
            "acceleration": a,
            "time": t,
            "initial_position": x0,
            "final_velocity": v,
            "final_position": x,
            "displacement": x - x0,
            "v_squared": v_sq,
            "equations": {
                "v = v0 + at": f"{v:.4f}",
                "x = x0 + v0*t + ½at²": f"{x:.4f}",
                "v² = v0² + 2a·Δx": f"{v_sq:.4f}"
            }
        }

    @staticmethod
    def projectile_motion(v0: float, angle_deg: float,
                          h0: float = 0.0,
                          g: float = 9.80665) -> Dict[str, Any]:
        """
        2D projectile motion.
        Returns: range, max height, time of flight, trajectory points.
        """
        angle_rad = math.radians(angle_deg)
        vx = v0 * math.cos(angle_rad)
        vy = v0 * math.sin(angle_rad)

        # Time of flight (solving 0 = h0 + vy*t - ½g*t²)
        discriminant = vy**2 + 2 * g * h0
        if discriminant < 0:
            return {"error": "Invalid parameters: projectile never lands"}
        t_flight = (vy + math.sqrt(discriminant)) / g

        # Range and max height
        x_range = vx * t_flight
        t_peak = vy / g
        y_max = h0 + vy * t_peak - 0.5 * g * t_peak**2

        # Trajectory
        t_arr = np.linspace(0, t_flight, 200)
        x_arr = vx * t_arr
        y_arr = h0 + vy * t_arr - 0.5 * g * t_arr**2

        return {
            "initial_velocity": v0,
            "angle_degrees": angle_deg,
            "initial_height": h0,
            "vx": vx, "vy": vy,
            "time_of_flight": t_flight,
            "range": x_range,
            "max_height": y_max,
            "time_to_peak": t_peak,
            "trajectory": {"x": x_arr.tolist(), "y": y_arr.tolist()}
        }

    @staticmethod
    def circular_motion(v: float, r: float, m: float = 1.0) -> Dict[str, Any]:
        """Uniform circular motion: centripetal acceleration, force, period."""
        a_c = v**2 / r
        F_c = m * a_c
        omega = v / r
        T = 2 * math.pi * r / v
        f = 1 / T
        return {
            "speed": v,
            "radius": r,
            "mass": m,
            "centripetal_acceleration": a_c,
            "centripetal_force": F_c,
            "angular_velocity_rad_s": omega,
            "period_s": T,
            "frequency_Hz": f
        }

    # ──────────────────────────────────────────────
    # Dynamics & Energy
    # ──────────────────────────────────────────────

    @staticmethod
    def newton_second_law(F: float, m: float) -> Dict[str, Any]:
        """F = ma → a = F/m."""
        a = F / m
        return {"force_N": F, "mass_kg": m, "acceleration_m_s2": a}

    @staticmethod
    def work_energy(F: float, d: float, theta_deg: float = 0.0) -> Dict[str, Any]:
        """Work W = F·d·cos(θ)."""
        theta_rad = math.radians(theta_deg)
        W = F * d * math.cos(theta_rad)
        return {
            "force_N": F,
            "distance_m": d,
            "angle_deg": theta_deg,
            "work_J": W
        }

    @staticmethod
    def kinetic_energy(m: float, v: float) -> Dict[str, Any]:
        """KE = ½mv²."""
        KE = 0.5 * m * v**2
        return {"mass_kg": m, "velocity_m_s": v, "kinetic_energy_J": KE}

    @staticmethod
    def potential_energy(m: float, h: float, g: float = 9.80665) -> Dict[str, Any]:
        """Gravitational PE = mgh."""
        PE = m * g * h
        return {"mass_kg": m, "height_m": h, "g": g, "potential_energy_J": PE}

    @staticmethod
    def conservation_of_energy(KE_initial: float, PE_initial: float,
                                PE_final: float) -> Dict[str, Any]:
        """Compute final KE from conservation: KE_f + PE_f = KE_i + PE_i."""
        E_total = KE_initial + PE_initial
        KE_final = E_total - PE_final
        v_final = math.sqrt(max(0, 2 * KE_final))  # Assuming m=1 for simplicity
        return {
            "total_energy_J": E_total,
            "initial_KE_J": KE_initial,
            "initial_PE_J": PE_initial,
            "final_PE_J": PE_final,
            "final_KE_J": KE_final
        }

    @staticmethod
    def momentum_collision(m1: float, v1: float, m2: float, v2: float,
                           collision_type: str = "elastic") -> Dict[str, Any]:
        """
        1D collision.
        collision_type: 'elastic' (KE conserved) or 'inelastic' (perfectly inelastic).
        """
        p_initial = m1 * v1 + m2 * v2
        if collision_type == "elastic":
            v1_f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
            v2_f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
            KE_before = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2
            KE_after = 0.5 * m1 * v1_f**2 + 0.5 * m2 * v2_f**2
        else:  # perfectly inelastic
            v_combined = p_initial / (m1 + m2)
            v1_f = v2_f = v_combined
            KE_before = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2
            KE_after = 0.5 * (m1 + m2) * v_combined**2
        return {
            "collision_type": collision_type,
            "before": {"m1": m1, "v1": v1, "m2": m2, "v2": v2},
            "momentum_initial": p_initial,
            "momentum_final": m1 * v1_f + m2 * v2_f,
            "v1_final": v1_f,
            "v2_final": v2_f,
            "KE_before_J": KE_before,
            "KE_after_J": KE_after,
            "KE_lost_J": KE_before - KE_after
        }

    # ──────────────────────────────────────────────
    # Thermodynamics
    # ──────────────────────────────────────────────

    @staticmethod
    def ideal_gas_law(P: Optional[float] = None, V: Optional[float] = None,
                      n: Optional[float] = None, T: Optional[float] = None) -> Dict[str, Any]:
        """
        PV = nRT. Solve for the missing variable (one of P, V, n, T must be None).
        P in Pa, V in m³, n in mol, T in K.
        """
        R = CONSTANTS["R"]
        given = {k: v for k, v in {"P": P, "V": V, "n": n, "T": T}.items() if v is not None}
        if len(given) != 3:
            raise ValueError("Provide exactly 3 of: P, V, n, T")
        if P is None:
            P = n * R * T / V
            solved = "P"
        elif V is None:
            V = n * R * T / P
            solved = "V"
        elif n is None:
            n = P * V / (R * T)
            solved = "n"
        else:
            T = P * V / (n * R)
            solved = "T"
        return {
            "P_Pa": P, "V_m3": V, "n_mol": n, "T_K": T,
            "R": R, "solved_for": solved,
            "equation": "PV = nRT"
        }

    @staticmethod
    def heat_transfer(Q: Optional[float] = None, m: Optional[float] = None,
                      c: Optional[float] = None, delta_T: Optional[float] = None) -> Dict[str, Any]:
        """Q = mcΔT. Solve for missing variable."""
        given = {k: v for k, v in {"Q": Q, "m": m, "c": c, "dT": delta_T}.items() if v is not None}
        if len(given) != 3:
            raise ValueError("Provide exactly 3 of: Q, m, c, delta_T")
        if Q is None:
            Q = m * c * delta_T; solved = "Q"
        elif m is None:
            m = Q / (c * delta_T); solved = "m"
        elif c is None:
            c = Q / (m * delta_T); solved = "c"
        else:
            delta_T = Q / (m * c); solved = "delta_T"
        return {"Q_J": Q, "m_kg": m, "c_J_kg_K": c, "delta_T_K": delta_T,
                "solved_for": solved, "equation": "Q = mcΔT"}

    @staticmethod
    def carnot_efficiency(T_hot: float, T_cold: float) -> Dict[str, Any]:
        """Carnot engine efficiency: η = 1 - T_cold/T_hot (in Kelvin)."""
        if T_hot <= T_cold:
            raise ValueError("T_hot must be greater than T_cold")
        eta = 1 - T_cold / T_hot
        return {
            "T_hot_K": T_hot, "T_cold_K": T_cold,
            "efficiency": eta,
            "efficiency_percent": eta * 100,
            "COP_heat_pump": T_hot / (T_hot - T_cold),
            "COP_refrigerator": T_cold / (T_hot - T_cold)
        }

    @staticmethod
    def entropy_change(Q: float, T: float) -> Dict[str, Any]:
        """ΔS = Q/T for reversible process."""
        delta_S = Q / T
        return {"Q_J": Q, "T_K": T, "delta_S_J_K": delta_S}

    # ──────────────────────────────────────────────
    # Electrostatics
    # ──────────────────────────────────────────────

    @staticmethod
    def coulombs_law(q1: float, q2: float, r: float) -> Dict[str, Any]:
        """
        Coulomb's law: F = k·q1·q2/r²
        Returns force magnitude and direction (attractive/repulsive).
        """
        k = 1 / (4 * math.pi * CONSTANTS["epsilon_0"])
        F = k * abs(q1) * abs(q2) / r**2
        same_sign = (q1 > 0) == (q2 > 0)
        return {
            "q1_C": q1, "q2_C": q2, "r_m": r,
            "k": k,
            "force_N": F,
            "direction": "repulsive" if same_sign else "attractive"
        }

    @staticmethod
    def electric_field(q: float, r: float) -> Dict[str, Any]:
        """Electric field E = kq/r² from point charge q at distance r."""
        k = 1 / (4 * math.pi * CONSTANTS["epsilon_0"])
        E = k * abs(q) / r**2
        return {"q_C": q, "r_m": r, "E_N_C": E,
                "direction": "outward" if q > 0 else "inward"}

    @staticmethod
    def ohms_law(V: Optional[float] = None, I: Optional[float] = None,
                 R: Optional[float] = None) -> Dict[str, Any]:
        """V = IR. Solve for missing variable. Also compute power P = VI."""
        given = {k: v for k, v in {"V": V, "I": I, "R": R}.items() if v is not None}
        if len(given) != 2:
            raise ValueError("Provide exactly 2 of: V, I, R")
        if V is None:
            V = I * R; solved = "V"
        elif I is None:
            I = V / R; solved = "I"
        else:
            R = V / I; solved = "R"
        P = V * I
        return {"V_volts": V, "I_amps": I, "R_ohms": R,
                "P_watts": P, "solved_for": solved}

    # ──────────────────────────────────────────────
    # Special Relativity
    # ──────────────────────────────────────────────

    @staticmethod
    def lorentz_factor(v: float) -> Dict[str, Any]:
        """Compute Lorentz factor γ = 1/√(1 - v²/c²)."""
        c = CONSTANTS["c"]
        if abs(v) >= c:
            raise ValueError("Speed must be less than c")
        beta = v / c
        gamma = 1 / math.sqrt(1 - beta**2)
        return {
            "v_m_s": v,
            "beta": beta,
            "gamma": gamma
        }

    @staticmethod
    def time_dilation(t0: float, v: float) -> Dict[str, Any]:
        """Time dilation: t = γ·t₀ (proper time t₀ in moving frame)."""
        lf = PhysicsEngine.lorentz_factor(v)
        gamma = lf["gamma"]
        t = gamma * t0
        return {
            "proper_time_s": t0,
            "v_m_s": v,
            "gamma": gamma,
            "dilated_time_s": t,
            "time_factor": gamma
        }

    @staticmethod
    def length_contraction(L0: float, v: float) -> Dict[str, Any]:
        """Length contraction: L = L₀/γ."""
        lf = PhysicsEngine.lorentz_factor(v)
        gamma = lf["gamma"]
        L = L0 / gamma
        return {
            "proper_length_m": L0,
            "v_m_s": v,
            "gamma": gamma,
            "contracted_length_m": L
        }

    @staticmethod
    def mass_energy_equivalence(m: float) -> Dict[str, Any]:
        """E = mc². Compute energy equivalent of mass."""
        c = CONSTANTS["c"]
        E = m * c**2
        return {
            "mass_kg": m,
            "c_m_s": c,
            "energy_J": E,
            "energy_MeV": E / 1.602e-13,
            "energy_eV": E / 1.602e-19
        }

    @staticmethod
    def relativistic_momentum(m: float, v: float) -> Dict[str, Any]:
        """p = γmv (relativistic momentum)."""
        lf = PhysicsEngine.lorentz_factor(v)
        gamma = lf["gamma"]
        p = gamma * m * v
        p_classical = m * v
        return {
            "rest_mass_kg": m,
            "v_m_s": v,
            "gamma": gamma,
            "relativistic_momentum": p,
            "classical_momentum": p_classical,
            "ratio": p / p_classical
        }

    # ──────────────────────────────────────────────
    # Quantum Mechanics
    # ──────────────────────────────────────────────

    @staticmethod
    def de_broglie_wavelength(m: float, v: float) -> Dict[str, Any]:
        """λ = h/(mv) — de Broglie wavelength."""
        h = CONSTANTS["h"]
        lamda = h / (m * v)
        return {
            "mass_kg": m,
            "velocity_m_s": v,
            "h": h,
            "wavelength_m": lamda,
            "wavelength_nm": lamda * 1e9
        }

    @staticmethod
    def heisenberg_uncertainty(delta_x: Optional[float] = None,
                               delta_p: Optional[float] = None) -> Dict[str, Any]:
        """
        Heisenberg uncertainty: Δx·Δp ≥ ℏ/2.
        Given one, compute minimum of the other.
        """
        hbar = CONSTANTS["hbar"]
        min_product = hbar / 2
        if delta_x is not None:
            min_delta_p = min_product / delta_x
            return {
                "delta_x_m": delta_x,
                "min_delta_p_kg_m_s": min_delta_p,
                "hbar_over_2": min_product
            }
        elif delta_p is not None:
            min_delta_x = min_product / delta_p
            return {
                "delta_p_kg_m_s": delta_p,
                "min_delta_x_m": min_delta_x,
                "hbar_over_2": min_product
            }
        else:
            raise ValueError("Provide either delta_x or delta_p")

    @staticmethod
    def photoelectric_effect(freq: float, work_function_eV: float) -> Dict[str, Any]:
        """
        Photoelectric effect: KE_max = hf - φ.
        freq in Hz, work_function in eV.
        """
        h = CONSTANTS["h"]
        eV = CONSTANTS["e"]
        E_photon = h * freq
        phi = work_function_eV * eV  # Convert to Joules
        KE_max = E_photon - phi
        return {
            "frequency_Hz": freq,
            "work_function_eV": work_function_eV,
            "E_photon_J": E_photon,
            "E_photon_eV": E_photon / eV,
            "KE_max_J": max(0, KE_max),
            "KE_max_eV": max(0, KE_max / eV),
            "electron_emitted": KE_max > 0,
            "threshold_frequency_Hz": phi / h
        }

    # ──────────────────────────────────────────────
    # Gravity & Orbital Mechanics
    # ──────────────────────────────────────────────

    @staticmethod
    def gravitational_force(m1: float, m2: float, r: float) -> Dict[str, Any]:
        """Newton's law of gravitation: F = Gm1m2/r²."""
        G = CONSTANTS["G"]
        F = G * m1 * m2 / r**2
        return {
            "m1_kg": m1, "m2_kg": m2, "r_m": r, "G": G,
            "force_N": F
        }

    @staticmethod
    def orbital_velocity(M: float, r: float) -> Dict[str, Any]:
        """Circular orbital speed: v = √(GM/r)."""
        G = CONSTANTS["G"]
        v = math.sqrt(G * M / r)
        T = 2 * math.pi * r / v
        return {
            "central_mass_kg": M,
            "orbital_radius_m": r,
            "orbital_velocity_m_s": v,
            "orbital_period_s": T,
            "orbital_period_hours": T / 3600,
            "orbital_period_days": T / 86400
        }

    @staticmethod
    def escape_velocity(M: float, r: float) -> Dict[str, Any]:
        """Escape velocity: v_esc = √(2GM/r)."""
        G = CONSTANTS["G"]
        v_esc = math.sqrt(2 * G * M / r)
        return {
            "body_mass_kg": M,
            "radius_m": r,
            "escape_velocity_m_s": v_esc,
            "escape_velocity_km_s": v_esc / 1000
        }

    # ──────────────────────────────────────────────
    # Wave Mechanics
    # ──────────────────────────────────────────────

    @staticmethod
    def wave_equation(v: Optional[float] = None, f: Optional[float] = None,
                      lamda: Optional[float] = None) -> Dict[str, Any]:
        """v = fλ. Solve for missing variable."""
        given = {k: val for k, val in {"v": v, "f": f, "lambda": lamda}.items() if val is not None}
        if len(given) != 2:
            raise ValueError("Provide exactly 2 of: v, f, lambda")
        if v is None:
            v = f * lamda; solved = "v"
        elif f is None:
            f = v / lamda; solved = "f"
        else:
            lamda = v / f; solved = "lambda"
        T = 1 / f
        omega = 2 * math.pi * f
        k = 2 * math.pi / lamda
        return {
            "wave_speed_m_s": v,
            "frequency_Hz": f,
            "wavelength_m": lamda,
            "period_s": T,
            "angular_frequency_rad_s": omega,
            "wave_number_rad_m": k,
            "solved_for": solved
        }

    @staticmethod
    def doppler_effect(f_source: float, v_sound: float,
                       v_observer: float = 0.0, v_source: float = 0.0,
                       observer_moving_toward: bool = True,
                       source_moving_toward: bool = False) -> Dict[str, Any]:
        """
        Doppler effect for sound.
        f_obs = f_s × (v ± v_o) / (v ∓ v_s)
        """
        vo_sign = 1 if observer_moving_toward else -1
        vs_sign = -1 if source_moving_toward else 1
        denom = v_sound + vs_sign * v_source
        if denom == 0:
            return {"error": "Source moving at speed of sound (singularity)"}
        f_obs = f_source * (v_sound + vo_sign * v_observer) / denom
        return {
            "source_frequency_Hz": f_source,
            "observed_frequency_Hz": f_obs,
            "frequency_shift_Hz": f_obs - f_source,
            "shift_percent": (f_obs - f_source) / f_source * 100,
            "v_sound_m_s": v_sound,
            "v_observer_m_s": v_observer,
            "v_source_m_s": v_source
        }
