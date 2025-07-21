# Summer Research Work Report
**Project Title**: UWB-Summer-Research - Hybrid Modulation Techniques in Ultra-Wideband Communication Systems  
**Research Period**: June 17, 2025 - July 15, 2025  
**Research Area**: Ultra-Wideband (UWB) Communications, Digital Modulation/Demodulation, Signal Processing  

## Project Overview

This summer research project focuses on the study of hybrid modulation techniques combining PPM (Pulse Position Modulation) and PSK (Phase Shift Keying) in Ultra-Wideband (UWB) communication systems. The project employs a combination of MATLAB Simulink and Python to achieve a complete UWB communication system research and implementation, covering signal simulation, noise modeling, and demodulation algorithm design.

## Research Timeline and Major Work Content

### Phase 1: Basic QPSK System Implementation (v1-v2)
**Timeline**: Early to Mid-June  
**Major Work**:
- **v1 - QPSK Symbol Synchronization System** (`myqpsk_symbol_sync.slx`)
  - Added symbol synchronization functionality to basic TX+RX architecture
  - Implemented QPSK system with 4GHz carrier frequency and 500MHz symbol rate
  - Set sampling rate to 40GHz with 750ps window length
  
- **v2 - Algorithm Optimization Version** (`myqpsk_optimized.slx`)
  - Algorithmic optimization based on v1
  - Enhanced system performance and processing efficiency

### Phase 2: UWB System Development and Sampling Rate Optimization (v3_250617)
**Timeline**: June 17  
**Major Breakthroughs**:
- **uwb_0**: Solved physical limitations of sampling rate
  - Used Cadence simulation-generated CSV data as input
  - Original sampling rate 16GHz → upsampled to 256GHz
  - Significantly improved time axis resolution, laying foundation for precise demodulation

- **uwb_2_nature256**: Attempted demodulation using native 256GHz sampling data
- **uwb_3_nature16**: Native 16GHz + upsampling to 256GHz + LPF interpolation demodulation
- **uwb_4_delay_mult**: Innovative DQPSK signal demodulation method
  - Implemented adjacent symbol differential calculation
  - Used delayed version multiplied with current symbol for IQ demodulation

**Technical Highlights**:
- Signal squaring detection + moving average filtering
- Peak detection and position analysis
- Completed Python data visualization tool development

### Phase 3: 8PSK Modulation and Constellation Calibration (v4_250623)
**Timeline**: June 23  
**Important Progress**:
- **8PSK Modulation System Implementation** (`uwb_0_8psk.slx`)
- **Automatic Constellation Calibration Algorithm** (`constellation_calibrate.ipynb`)
  - Used K-means clustering algorithm for automatic constellation point identification
  - Implemented Gray code mapping optimization
  - Precise positioning and angular sorting of 8 constellation points

**Performance Analysis**:
- Completed 8PSK demodulation algorithm
- Implemented IQ separation processing for complex signals
- Developed Bit Error Rate (BER) analysis tools

### Phase 4: Noise Modeling and PPM-PSK Hybrid Modulation (v5_250626)
**Timeline**: June 26  
**Core Work**:
- **Phase Noise Modeling** (`phase_noise_*.ipynb`)
  - Implemented time jitter noise conversion: Δt = Δφ / (2π × f_carrier)
  - AWGN noise addition and SNR control
  - Noise characteristic analysis under 4GHz carrier frequency

- **PPM-PSK Hybrid Modulation** (`ppm_psk_shared_v3.slx`)
  - 8PPM + D2PSK combined modulation scheme
  - PPM spacing optimization: 8 positions within 698-1299ps range
  - Hybrid modulation demodulation algorithm design

- **Ground Truth Data Generation** (`create_ground_truth.ipynb`)
  - Created reference data at 256GHz sampling rate
  - Generated ideal signals in noise-free environment

### Phase 5: High Sampling Rate Systems and Parameter Optimization (v6_250708)
**Timeline**: July 8  
**Technical Improvements**:
- **Ultra-High Sampling Rate Implementation**: Upsampling to 1.024THz (1024GHz)
- **Fine PPM Spacing Adjustment**: Redesigned spacing parameters
  - ppm_spacings2_ps = [-51.8, 33.2, 115.3, 201.3, 293.8, 377.9, 462.9, 544.9]
- **In-Depth Phase Noise Research**
  - Completed phase noise analysis in collaboration with Peter Michael
  - Precise modeling of time jitter noise

### Phase 6: Template Matching Algorithm Research (v7_250710)
**Timeline**: July 10  
**Algorithm Innovation**:
- **Template Matching Demodulation** (`template_matching.py`)
  - Correlation-based pulse position detection
  - phase0/phase1 template generation and matching
  - Enhanced PPM signal detection accuracy

- **Template Extraction Tool** (`extract_templates.py`)
- **Visualization Analysis** (`plot_templates.py`)

### Phase 7: Final Integrated System (v8_250715)
**Timeline**: July 15  
**Final Results**:
- **Complete 2PPM+8PSK Demodulation System** (`demod_2ppm_8psk.ipynb`)
  - Integrated all previous research achievements
  - Complete signal processing pipeline:
    1. Phase noise addition
    2. AWGN noise modeling (SNR=20dB)
    3. Downsampling to 32GHz
    4. Upsampling to 1024GHz
    5. Data folding and periodic analysis
    6. Edge detection and midpoint calculation
    7. 2-cluster PPM demodulation
    8. IQ demodulation and 8PSK symbol decision

- **Performance Evaluation Completed**:
  - PPM bit error rate analysis
  - 8PSK bit error rate analysis
  - RMS BER calculation

## Technical Architecture and Innovation Points

### 1. Signal Processing Pipeline
```
Cadence Simulation Data → Phase Noise Addition → AWGN Noise → Sampling Rate Conversion → 
PPM Demodulation → IQ Demodulation → 8PSK Demodulation → Performance Evaluation
```

### 2. Key Technical Innovations
- **Sampling Rate Optimization Strategy**: Multi-stage upsampling from 16GHz → 1024GHz
- **Hybrid Modulation Scheme**: Efficient combination of 2PPM + 8PSK
- **Noise Modeling Precision**: Accurate conversion from phase noise to time jitter
- **Adaptive Demodulation**: Automatic constellation calibration using K-means clustering

### 3. Algorithm Highlights
- **Edge Detection Algorithm**: Butterworth filtering + threshold detection
- **Clustering Classification**: Simplified PPM classification scheme with 1ns threshold
- **Symbol Alignment**: Dynamic offset correction algorithm

## Research Results and Data

### System Parameters
- **Carrier Frequency**: 4GHz
- **Symbol Rate**: 500MHz (2ns symbol period)
- **Modulation Scheme**: 2PPM + 8PSK
- **Final Sampling Rate**: 1024GHz
- **Signal-to-Noise Ratio**: 20dB
- **Phase Noise**: Configurable standard deviation

### Performance Metrics
- **PPM Demodulation Accuracy**: Precise position detection through 2-cluster algorithm
- **8PSK Constellation**: Accurate identification of 8 equally-spaced phase points
- **Overall BER**: RMS bit error rate evaluation completed

### Output Data
- Large-scale CSV data files (50MB+ scale)
- Complete reference datasets
- Noise characteristic analysis data

## Tools and Technology Stack

### Development Environment
- **MATLAB R2025a**: Simulink modeling and simulation
- **Python**: NumPy, Pandas, SciPy, Matplotlib
- **Cadence**: RF circuit simulation data generation

### Core Algorithm Libraries
- **scikit-learn**: K-means clustering algorithm
- **SciPy**: Signal processing and filtering
- **NumPy**: High-performance numerical computation

## Project Management and Version Control

Git-based version management with clear timeline documentation of progress at each stage:
- 8 major versions (v1 → v8_250715)
- Complete code history tracking
- Modular functional development

## Research Significance and Application Prospects

### Academic Value
1. **Hybrid Modulation Technology**: Application research of PPM and PSK combination in UWB systems
2. **High Sampling Rate Processing**: Signal processing algorithm optimization at THz-level sampling rates
3. **Noise Modeling**: Precise modeling methods for phase noise and time jitter

### Practical Applications
1. **UWB Communication Systems**: Providing technical foundation for next-generation ultra-wideband communications
2. **High-Speed Data Transmission**: Efficient demodulation solutions for 500Mbps symbol rates
3. **Noise-Resistant Design**: Robust design suitable for harsh channel environments

## Conclusions

This summer's research work began with basic QPSK systems and gradually developed into a complete UWB hybrid modulation communication system. Through nearly one month of continuous effort, the following achievements were successfully realized:

1. **Complete System Design**: Full-link implementation from transmission to reception
2. **Algorithm Innovation**: Comparison and optimization of multiple demodulation algorithms
3. **Performance Verification**: Detailed bit error rate analysis and performance evaluation
4. **Engineering Practice**: Large-scale data processing and visualization analysis

This project not only deepened understanding of digital communication theory but also provided valuable engineering experience through actual algorithm implementation and system integration. The research results lay a solid technical foundation for further development of UWB communication systems.

## Key Contributions

### Technical Contributions
- **Novel Hybrid Modulation Approach**: Successfully demonstrated the feasibility of 2PPM+8PSK combination in UWB systems
- **Advanced Sampling Rate Management**: Developed efficient multi-stage upsampling techniques reaching THz-level processing
- **Robust Demodulation Algorithms**: Created adaptive algorithms capable of handling both PPM and PSK components simultaneously
- **Comprehensive Noise Modeling**: Established precise phase noise to time jitter conversion methodologies

### Methodological Contributions
- **Systematic Development Approach**: Demonstrated incremental development from basic QPSK to complex hybrid systems
- **Multi-Tool Integration**: Successfully combined MATLAB Simulink with Python for comprehensive system development
- **Performance Optimization**: Achieved significant improvements in demodulation accuracy through iterative algorithm refinement

### Future Work Directions
- **Real-Time Implementation**: Adaptation of algorithms for real-time hardware implementation
- **Extended Modulation Orders**: Investigation of higher-order PPM and PSK combinations
- **Advanced Channel Models**: Integration of more complex channel impairments and mitigation techniques
- **Machine Learning Integration**: Potential application of ML techniques for adaptive demodulation

---
*Report Generated: July 21, 2025*  
*Project Repository: UWB-Summer-Research (GitHub: Ken-2511)*
