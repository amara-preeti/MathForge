"""FastAPI router for Physics Engine."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from physics_engine.engine import PhysicsEngine

router = APIRouter(prefix="/physics", tags=["Physics"])
engine = PhysicsEngine()


class Kinematics1DRequest(BaseModel):
    v0: float
    a: float
    t: float
    x0: float = 0.0

class ProjectileRequest(BaseModel):
    v0: float
    angle_deg: float
    h0: float = 0.0
    g: float = 9.80665

class CircularMotionRequest(BaseModel):
    v: float
    r: float
    m: float = 1.0

class Newton2Request(BaseModel):
    F: float
    m: float

class WorkRequest(BaseModel):
    F: float
    d: float
    theta_deg: float = 0.0

class KERequest(BaseModel):
    m: float
    v: float

class PERequest(BaseModel):
    m: float
    h: float
    g: float = 9.80665

class CollisionRequest(BaseModel):
    m1: float
    v1: float
    m2: float
    v2: float
    collision_type: str = "elastic"

class IdealGasRequest(BaseModel):
    P: Optional[float] = None
    V: Optional[float] = None
    n: Optional[float] = None
    T: Optional[float] = None

class HeatTransferRequest(BaseModel):
    Q: Optional[float] = None
    m: Optional[float] = None
    c: Optional[float] = None
    delta_T: Optional[float] = None

class CarnotRequest(BaseModel):
    T_hot: float
    T_cold: float

class EntropyRequest(BaseModel):
    Q: float
    T: float

class CoulombRequest(BaseModel):
    q1: float
    q2: float
    r: float

class ElectricFieldRequest(BaseModel):
    q: float
    r: float

class OhmsRequest(BaseModel):
    V: Optional[float] = None
    I: Optional[float] = None
    R: Optional[float] = None

class LorentzRequest(BaseModel):
    v: float

class TimeDilationRequest(BaseModel):
    t0: float
    v: float

class LengthContractionRequest(BaseModel):
    L0: float
    v: float

class MassEnergyRequest(BaseModel):
    m: float

class DeBroglieRequest(BaseModel):
    m: float
    v: float

class HeisenbergRequest(BaseModel):
    delta_x: Optional[float] = None
    delta_p: Optional[float] = None

class PhotoelectricRequest(BaseModel):
    freq: float
    work_function_eV: float

class GravityRequest(BaseModel):
    m1: float
    m2: float
    r: float

class OrbitalRequest(BaseModel):
    M: float
    r: float

class EscapeVelocityRequest(BaseModel):
    M: float
    r: float

class WaveRequest(BaseModel):
    v: Optional[float] = None
    f: Optional[float] = None
    lamda: Optional[float] = None

class DopplerRequest(BaseModel):
    f_source: float
    v_sound: float
    v_observer: float = 0.0
    v_source: float = 0.0
    observer_moving_toward: bool = True
    source_moving_toward: bool = False


@router.get("/constants")
def get_constants():
    return engine.get_constants()

@router.post("/kinematics-1d")
def kinematics_1d(req: Kinematics1DRequest):
    try:
        return engine.kinematics_1d(req.v0, req.a, req.t, req.x0)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/projectile-motion")
def projectile_motion(req: ProjectileRequest):
    try:
        return engine.projectile_motion(req.v0, req.angle_deg, req.h0, req.g)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/circular-motion")
def circular_motion(req: CircularMotionRequest):
    try:
        return engine.circular_motion(req.v, req.r, req.m)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/newton-second-law")
def newton_second(req: Newton2Request):
    try:
        return engine.newton_second_law(req.F, req.m)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/work")
def work_energy(req: WorkRequest):
    try:
        return engine.work_energy(req.F, req.d, req.theta_deg)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/kinetic-energy")
def kinetic_energy(req: KERequest):
    try:
        return engine.kinetic_energy(req.m, req.v)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/potential-energy")
def potential_energy(req: PERequest):
    try:
        return engine.potential_energy(req.m, req.h, req.g)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/collision")
def collision(req: CollisionRequest):
    try:
        return engine.momentum_collision(req.m1, req.v1, req.m2, req.v2, req.collision_type)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/ideal-gas")
def ideal_gas(req: IdealGasRequest):
    try:
        return engine.ideal_gas_law(req.P, req.V, req.n, req.T)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/heat-transfer")
def heat_transfer(req: HeatTransferRequest):
    try:
        return engine.heat_transfer(req.Q, req.m, req.c, req.delta_T)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/carnot")
def carnot(req: CarnotRequest):
    try:
        return engine.carnot_efficiency(req.T_hot, req.T_cold)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/entropy")
def entropy(req: EntropyRequest):
    try:
        return engine.entropy_change(req.Q, req.T)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/coulombs-law")
def coulombs_law(req: CoulombRequest):
    try:
        return engine.coulombs_law(req.q1, req.q2, req.r)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/electric-field")
def electric_field(req: ElectricFieldRequest):
    try:
        return engine.electric_field(req.q, req.r)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/ohms-law")
def ohms_law(req: OhmsRequest):
    try:
        return engine.ohms_law(req.V, req.I, req.R)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/lorentz-factor")
def lorentz_factor(req: LorentzRequest):
    try:
        return engine.lorentz_factor(req.v)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/time-dilation")
def time_dilation(req: TimeDilationRequest):
    try:
        return engine.time_dilation(req.t0, req.v)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/length-contraction")
def length_contraction(req: LengthContractionRequest):
    try:
        return engine.length_contraction(req.L0, req.v)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/mass-energy")
def mass_energy(req: MassEnergyRequest):
    try:
        return engine.mass_energy_equivalence(req.m)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/de-broglie")
def de_broglie(req: DeBroglieRequest):
    try:
        return engine.de_broglie_wavelength(req.m, req.v)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/heisenberg")
def heisenberg(req: HeisenbergRequest):
    try:
        return engine.heisenberg_uncertainty(req.delta_x, req.delta_p)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/photoelectric")
def photoelectric(req: PhotoelectricRequest):
    try:
        return engine.photoelectric_effect(req.freq, req.work_function_eV)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/gravity")
def gravity(req: GravityRequest):
    try:
        return engine.gravitational_force(req.m1, req.m2, req.r)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/orbital-velocity")
def orbital_velocity(req: OrbitalRequest):
    try:
        return engine.orbital_velocity(req.M, req.r)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/escape-velocity")
def escape_velocity(req: EscapeVelocityRequest):
    try:
        return engine.escape_velocity(req.M, req.r)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/wave")
def wave(req: WaveRequest):
    try:
        return engine.wave_equation(req.v, req.f, req.lamda)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/doppler")
def doppler(req: DopplerRequest):
    try:
        return engine.doppler_effect(req.f_source, req.v_sound, req.v_observer,
                                     req.v_source, req.observer_moving_toward,
                                     req.source_moving_toward)
    except Exception as e:
        raise HTTPException(400, str(e))
