"""
Signal Processing Engine
========================
Comprehensive digital signal processing module covering:
- Discrete Fourier Transform (DFT/FFT) and inverse
- Power spectral density (Welch, periodogram)
- FIR/IIR filter design and application
- Convolution and correlation
- Windowing functions
- Short-time Fourier Transform (STFT)
- Autocorrelation / cross-correlation
- Signal generation (sine, square, sawtooth, chirp, noise)
- Filtering (lowpass, highpass, bandpass, bandstop)
"""

from __future__ import annotations
import numpy as np
from numpy.fft import fft, ifft, fftfreq, rfft, irfft, rfftfreq
from scipy import signal as scipy_signal
from scipy.signal import (
    butter, cheby1, cheby2, ellip, bessel,
    firwin, firwin2, remez,
    lfilter, sosfilt, filtfilt,
    freqz, freqs, group_delay,
    welch, periodogram, spectrogram,
    correlate, convolve,
    find_peaks, peak_prominences, peak_widths,
    chirp as scipy_chirp,
    stft as scipy_stft, istft,
    get_window
)
from typing import Dict, Any, List, Optional, Tuple


class SignalProcessingEngine:
    """Full-featured digital signal processing engine."""

    # ──────────────────────────────────────────────
    # Signal Generation
    # ──────────────────────────────────────────────

    @staticmethod
    def generate_sine(freq: float, duration: float, sample_rate: int = 44100,
                      amplitude: float = 1.0, phase: float = 0.0) -> Dict[str, Any]:
        """Generate a pure sine wave."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        y = amplitude * np.sin(2 * np.pi * freq * t + phase)
        return {
            "type": "sine",
            "frequency": freq,
            "duration": duration,
            "sample_rate": sample_rate,
            "amplitude": amplitude,
            "phase": phase,
            "t": t.tolist(),
            "y": y.tolist(),
            "num_samples": len(t)
        }

    @staticmethod
    def generate_square(freq: float, duration: float, sample_rate: int = 44100,
                        amplitude: float = 1.0, duty: float = 0.5) -> Dict[str, Any]:
        """Generate a square wave with given duty cycle."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        y = amplitude * scipy_signal.square(2 * np.pi * freq * t, duty=duty)
        return {
            "type": "square",
            "frequency": freq,
            "duration": duration,
            "sample_rate": sample_rate,
            "duty_cycle": duty,
            "t": t.tolist(),
            "y": y.tolist()
        }

    @staticmethod
    def generate_sawtooth(freq: float, duration: float, sample_rate: int = 44100,
                          amplitude: float = 1.0, width: float = 1.0) -> Dict[str, Any]:
        """Generate a sawtooth wave (width=1 → rising, width=0 → falling)."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        y = amplitude * scipy_signal.sawtooth(2 * np.pi * freq * t, width=width)
        return {
            "type": "sawtooth",
            "frequency": freq,
            "duration": duration,
            "sample_rate": sample_rate,
            "width": width,
            "t": t.tolist(),
            "y": y.tolist()
        }

    @staticmethod
    def generate_chirp(f0: float, f1: float, duration: float,
                       sample_rate: int = 44100, method: str = "linear") -> Dict[str, Any]:
        """Generate a frequency-swept chirp signal."""
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        y = scipy_chirp(t, f0=f0, f1=f1, t1=duration, method=method)
        return {
            "type": "chirp",
            "f0": f0, "f1": f1,
            "duration": duration,
            "sample_rate": sample_rate,
            "method": method,
            "t": t.tolist(),
            "y": y.tolist()
        }

    @staticmethod
    def generate_noise(noise_type: str, duration: float, sample_rate: int = 44100,
                       amplitude: float = 1.0) -> Dict[str, Any]:
        """Generate noise: 'white', 'pink', or 'gaussian'."""
        n = int(sample_rate * duration)
        t = np.linspace(0, duration, n, endpoint=False)
        if noise_type == "white":
            y = amplitude * np.random.uniform(-1, 1, n)
        elif noise_type == "gaussian":
            y = amplitude * np.random.randn(n)
        elif noise_type == "pink":
            # Voss-McCartney algorithm
            f = np.fft.rfftfreq(n)
            f[0] = 1  # avoid division by zero
            power = 1.0 / np.sqrt(f)
            power[0] = 0
            phases = np.random.uniform(0, 2 * np.pi, len(f))
            spectrum = power * np.exp(1j * phases)
            y = np.fft.irfft(spectrum, n=n)
            y = amplitude * y / np.max(np.abs(y))
        else:
            raise ValueError(f"Unknown noise type: {noise_type}")
        return {
            "type": f"{noise_type}_noise",
            "duration": duration,
            "sample_rate": sample_rate,
            "t": t.tolist(),
            "y": y.tolist()
        }

    # ──────────────────────────────────────────────
    # Fourier Transform
    # ──────────────────────────────────────────────

    @staticmethod
    def compute_fft(signal_data: List[float], sample_rate: int = 44100) -> Dict[str, Any]:
        """Compute the FFT of a signal and return magnitude/phase spectra."""
        y = np.array(signal_data)
        n = len(y)
        yf = rfft(y)
        xf = rfftfreq(n, 1.0 / sample_rate)
        magnitude = np.abs(yf) * 2 / n
        magnitude[0] /= 2  # DC component not doubled
        phase = np.angle(yf, deg=True)
        power_db = 20 * np.log10(magnitude + 1e-12)
        return {
            "frequencies": xf.tolist(),
            "magnitude": magnitude.tolist(),
            "phase_degrees": phase.tolist(),
            "power_db": power_db.tolist(),
            "num_samples": n,
            "sample_rate": sample_rate,
            "frequency_resolution": sample_rate / n
        }

    @staticmethod
    def compute_ifft(spectrum_real: List[float], spectrum_imag: List[float],
                     n: Optional[int] = None) -> Dict[str, Any]:
        """Reconstruct signal from FFT spectrum."""
        spectrum = np.array(spectrum_real) + 1j * np.array(spectrum_imag)
        y = irfft(spectrum, n=n)
        return {"reconstructed_signal": y.tolist(), "num_samples": len(y)}

    @staticmethod
    def compute_stft(signal_data: List[float], sample_rate: int = 44100,
                     window_size: int = 256, hop_size: int = 128,
                     window: str = "hann") -> Dict[str, Any]:
        """Compute the Short-Time Fourier Transform (spectrogram)."""
        y = np.array(signal_data)
        f, t, Zxx = scipy_stft(y, fs=sample_rate, nperseg=window_size,
                                noverlap=window_size - hop_size, window=window)
        magnitude = np.abs(Zxx)
        return {
            "frequencies": f.tolist(),
            "times": t.tolist(),
            "magnitude": magnitude.tolist(),
            "window_size": window_size,
            "hop_size": hop_size
        }

    @staticmethod
    def compute_spectrogram(signal_data: List[float], sample_rate: int = 44100,
                            window_size: int = 256) -> Dict[str, Any]:
        """Compute power spectrogram using scipy.signal.spectrogram."""
        y = np.array(signal_data)
        f, t, Sxx = spectrogram(y, fs=sample_rate, nperseg=window_size)
        Sxx_db = 10 * np.log10(Sxx + 1e-12)
        return {
            "frequencies": f.tolist(),
            "times": t.tolist(),
            "power_db": Sxx_db.tolist()
        }

    # ──────────────────────────────────────────────
    # Power Spectral Density
    # ──────────────────────────────────────────────

    @staticmethod
    def welch_psd(signal_data: List[float], sample_rate: int = 44100,
                  nperseg: int = 256) -> Dict[str, Any]:
        """Estimate PSD using Welch's method."""
        y = np.array(signal_data)
        f, Pxx = welch(y, fs=sample_rate, nperseg=nperseg)
        Pxx_db = 10 * np.log10(Pxx + 1e-12)
        return {
            "frequencies": f.tolist(),
            "psd": Pxx.tolist(),
            "psd_db": Pxx_db.tolist(),
            "method": "welch",
            "nperseg": nperseg
        }

    @staticmethod
    def periodogram_psd(signal_data: List[float], sample_rate: int = 44100) -> Dict[str, Any]:
        """Estimate PSD using the periodogram method."""
        y = np.array(signal_data)
        f, Pxx = periodogram(y, fs=sample_rate)
        Pxx_db = 10 * np.log10(Pxx + 1e-12)
        return {
            "frequencies": f.tolist(),
            "psd": Pxx.tolist(),
            "psd_db": Pxx_db.tolist(),
            "method": "periodogram"
        }

    # ──────────────────────────────────────────────
    # Filter Design
    # ──────────────────────────────────────────────

    @staticmethod
    def design_butterworth(filter_type: str, cutoff: Any, order: int = 5,
                           sample_rate: int = 44100) -> Dict[str, Any]:
        """
        Design a Butterworth filter.
        filter_type: 'lowpass', 'highpass', 'bandpass', 'bandstop'
        cutoff: single freq for LP/HP, [low, high] for BP/BS
        """
        nyq = sample_rate / 2.0
        if isinstance(cutoff, list):
            norm_cutoff = [c / nyq for c in cutoff]
        else:
            norm_cutoff = cutoff / nyq
        sos = butter(order, norm_cutoff, btype=filter_type, output="sos")
        w, h = freqz(butter(order, norm_cutoff, btype=filter_type)[1],
                     butter(order, norm_cutoff, btype=filter_type)[0], worN=8000)
        freq_resp = (w / np.pi * nyq).tolist()
        mag_db = (20 * np.log10(np.abs(h) + 1e-12)).tolist()
        phase_deg = (np.angle(h, deg=True)).tolist()
        return {
            "filter_type": "butterworth",
            "btype": filter_type,
            "cutoff": cutoff,
            "order": order,
            "sample_rate": sample_rate,
            "sos": sos.tolist(),
            "frequency_response": {"freq": freq_resp, "magnitude_db": mag_db, "phase_deg": phase_deg}
        }

    @staticmethod
    def design_fir(filter_type: str, cutoff: Any, num_taps: int = 101,
                   window: str = "hamming", sample_rate: int = 44100) -> Dict[str, Any]:
        """Design an FIR filter using the window method."""
        nyq = sample_rate / 2.0
        if isinstance(cutoff, list):
            norm_cutoff = [c / nyq for c in cutoff]
        else:
            norm_cutoff = cutoff / nyq
        taps = firwin(num_taps, norm_cutoff, window=window, pass_zero=(filter_type == "lowpass"))
        w, h = freqz(taps, worN=8000)
        return {
            "filter_type": "fir",
            "btype": filter_type,
            "cutoff": cutoff,
            "num_taps": num_taps,
            "window": window,
            "taps": taps.tolist(),
            "frequency_response": {
                "freq": (w / np.pi * nyq).tolist(),
                "magnitude_db": (20 * np.log10(np.abs(h) + 1e-12)).tolist()
            }
        }

    # ──────────────────────────────────────────────
    # Filtering
    # ──────────────────────────────────────────────

    @staticmethod
    def apply_filter(signal_data: List[float], sos: List[List[float]],
                     method: str = "sosfiltfilt") -> Dict[str, Any]:
        """Apply a filter (given as SOS) to a signal."""
        y = np.array(signal_data)
        sos_arr = np.array(sos)
        if method == "sosfiltfilt":
            filtered = scipy_signal.sosfiltfilt(sos_arr, y)
        elif method == "sosfilt":
            filtered = sosfilt(sos_arr, y)
        else:
            raise ValueError(f"Unknown method: {method}")
        return {
            "original": signal_data,
            "filtered": filtered.tolist(),
            "method": method,
            "num_samples": len(filtered)
        }

    @staticmethod
    def moving_average(signal_data: List[float], window: int) -> Dict[str, Any]:
        """Apply a moving average (box filter)."""
        y = np.array(signal_data)
        kernel = np.ones(window) / window
        smoothed = np.convolve(y, kernel, mode="same")
        return {
            "original": signal_data,
            "smoothed": smoothed.tolist(),
            "window_size": window
        }

    # ──────────────────────────────────────────────
    # Convolution & Correlation
    # ──────────────────────────────────────────────

    @staticmethod
    def convolve_signals(x: List[float], h: List[float], mode: str = "full") -> Dict[str, Any]:
        """Convolve two signals."""
        result = convolve(np.array(x), np.array(h), mode=mode)
        return {
            "mode": mode,
            "input_lengths": [len(x), len(h)],
            "output_length": len(result),
            "result": result.tolist()
        }

    @staticmethod
    def cross_correlate(x: List[float], y: List[float]) -> Dict[str, Any]:
        """Compute cross-correlation of two signals."""
        corr = correlate(np.array(x), np.array(y), mode="full")
        lags = np.arange(-(len(y) - 1), len(x))
        peak_idx = int(np.argmax(np.abs(corr)))
        return {
            "correlation": corr.tolist(),
            "lags": lags.tolist(),
            "peak_lag": int(lags[peak_idx]),
            "peak_value": float(corr[peak_idx])
        }

    @staticmethod
    def autocorrelate(signal_data: List[float]) -> Dict[str, Any]:
        """Compute autocorrelation of a signal."""
        y = np.array(signal_data)
        corr = correlate(y, y, mode="full")
        corr /= corr[len(y) - 1]  # Normalize
        lags = np.arange(-(len(y) - 1), len(y))
        return {
            "autocorrelation": corr.tolist(),
            "lags": lags.tolist(),
            "normalized": True
        }

    # ──────────────────────────────────────────────
    # Peak Detection
    # ──────────────────────────────────────────────

    @staticmethod
    def find_signal_peaks(signal_data: List[float], height: Optional[float] = None,
                          threshold: Optional[float] = None,
                          distance: Optional[int] = None,
                          prominence: Optional[float] = None) -> Dict[str, Any]:
        """Find peaks in a signal with optional constraints."""
        y = np.array(signal_data)
        kwargs = {}
        if height is not None:
            kwargs["height"] = height
        if threshold is not None:
            kwargs["threshold"] = threshold
        if distance is not None:
            kwargs["distance"] = distance
        if prominence is not None:
            kwargs["prominence"] = prominence
        peaks, props = find_peaks(y, **kwargs)
        proms, _, _ = peak_prominences(y, peaks)
        widths, _, _, _ = peak_widths(y, peaks)
        return {
            "peak_indices": peaks.tolist(),
            "peak_values": y[peaks].tolist(),
            "prominences": proms.tolist(),
            "widths": widths.tolist(),
            "count": len(peaks)
        }

    # ──────────────────────────────────────────────
    # Windowing Functions
    # ──────────────────────────────────────────────

    @staticmethod
    def get_window_function(window_type: str, n_points: int) -> Dict[str, Any]:
        """Return a window function of given type and length."""
        w = get_window(window_type, n_points)
        return {
            "window_type": window_type,
            "n_points": n_points,
            "window": w.tolist(),
            "coherent_gain": float(np.mean(w)),
            "power_gain": float(np.mean(w**2))
        }

    # ──────────────────────────────────────────────
    # Signal Statistics
    # ──────────────────────────────────────────────

    @staticmethod
    def signal_statistics(signal_data: List[float], sample_rate: int = 44100) -> Dict[str, Any]:
        """Compute comprehensive statistics of a signal."""
        y = np.array(signal_data)
        rms = float(np.sqrt(np.mean(y**2)))
        crest = float(np.max(np.abs(y)) / rms) if rms > 0 else float("inf")
        return {
            "num_samples": len(y),
            "duration_s": len(y) / sample_rate,
            "sample_rate": sample_rate,
            "min": float(np.min(y)),
            "max": float(np.max(y)),
            "mean": float(np.mean(y)),
            "std": float(np.std(y)),
            "rms": rms,
            "peak": float(np.max(np.abs(y))),
            "crest_factor": crest,
            "kurtosis": float(scipy_signal.kurtosis(y) if hasattr(scipy_signal, "kurtosis") else 0),
            "zero_crossings": int(np.sum(np.diff(np.sign(y)) != 0))
        }

    @staticmethod
    def snr_estimate(signal_data: List[float], noise_data: List[float]) -> Dict[str, Any]:
        """Estimate Signal-to-Noise Ratio (SNR) in dB."""
        s = np.array(signal_data)
        n = np.array(noise_data)
        signal_power = np.mean(s**2)
        noise_power = np.mean(n**2)
        if noise_power == 0:
            return {"snr_db": float("inf"), "signal_power": float(signal_power), "noise_power": 0.0}
        snr = 10 * np.log10(signal_power / noise_power)
        return {
            "snr_db": float(snr),
            "signal_power": float(signal_power),
            "noise_power": float(noise_power)
        }
