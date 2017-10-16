"""
QUIMB
-----

Quantum Information for Many-Body calculations.
"""

# Accelerated basic linalg operations
from .accel import (
    prod,
    isket,
    isbra,
    isop,
    isvec,
    issparse,
    isherm,
    mul,
    dot,
    vdot,
    rdot,
    ldmul,
    rdmul,
    outer,
    explt,
)

# Core functions
from .core import (
    normalize,
    chop,
    quimbify,
    qu,
    ket,
    bra,
    dop,
    sparse,
    infer_size,
    trace,
    identity,
    eye,
    speye,
    dim_map,
    dim_compress,
    kron,
    kronpow,
    eyepad,
    perm_eyepad,
    permute,
    itrace,
    partial_trace,
    expectation,
    expec,
    overlap,
    nmlz,
    tr,
    ptr,
)

# Linear algebra functions
from .linalg.base_linalg import (
    eigsys,
    eigvals,
    eigvecs,
    seigsys,
    seigvals,
    seigvecs,
    groundstate,
    groundenergy,
    bound_spectrum,
    eigsys_window,
    eigvals_window,
    eigvecs_window,
    svd,
    svds,
    norm,
    expm,
    sqrtm,
    expm_multiply,
)

# Generating objects
from .gen.operators import (
    spin_operator,
    sig,
    controlled,
    ham_heis,
    ham_j1j2,
    zspin_projector,
    swap,
)
from .gen.states import (
    basis_vec,
    up,
    zplus,
    down,
    zminus,
    plus,
    xplus,
    minus,
    xminus,
    yplus,
    yminus,
    bloch_state,
    bell_state,
    singlet,
    thermal_state,
    neel_state,
    singlet_pairs,
    werner_state,
    ghz_state,
    w_state,
    levi_civita,
    perm_state,
    graph_state_1d,
)
from .gen.rand import (
    rand_matrix,
    rand_herm,
    rand_pos,
    rand_rho,
    rand_ket,
    rand_uni,
    rand_haar_state,
    gen_rand_haar_states,
    rand_mix,
    rand_product_state,
    rand_matrix_product_state,
    rand_mps,
    rand_seperable,
)

# Functions for calculating properties
from .calc import (
    fidelity,
    purify,
    entropy,
    entropy_subsys,
    mutual_information,
    mutinf,
    mutinf_subsys,
    partial_transpose,
    negativity,
    logarithmic_negativity,
    logneg,
    logneg_subsys,
    concurrence,
    one_way_classical_information,
    quantum_discord,
    trace_distance,
    decomp,
    pauli_decomp,
    bell_decomp,
    correlation,
    pauli_correlations,
    ent_cross_matrix,
    qid,
    is_degenerate,
    is_eigenvector,
    page_entropy,
)

# Evolution class and methods
from .evo import QuEvo

from .linalg.approx_spectral import (
    approx_spectral_function,
    tr_abs_approx,
    tr_exp_approx,
    tr_sqrt_approx,
    tr_xlogx_approx,
    entropy_subsys_approx,
    logneg_subsys_approx,
    negativity_subsys_approx,
)


__all__ = [
    # Accel ----------------------------------------------------------------- #
    'prod',
    'isket',
    'isbra',
    'isop',
    'isvec',
    'issparse',
    'isherm',
    'mul',
    'dot',
    'vdot',
    'rdot',
    'ldmul',
    'rdmul',
    'outer',
    'explt',
    # Core ------------------------------------------------------------------ #
    'normalize',
    'chop',
    'quimbify',
    'qu',
    'ket',
    'bra',
    'dop',
    'sparse',
    'infer_size',
    'trace',
    'identity',
    'eye',
    'speye',
    'dim_map',
    'dim_compress',
    'kron',
    'kronpow',
    'eyepad',
    'perm_eyepad',
    'permute',
    'itrace',
    'partial_trace',
    'expectation',
    'expec',
    'overlap',
    'nmlz',
    'tr',
    'ptr',
    # Linalg ---------------------------------------------------------------- #
    'eigsys',
    'eigvals',
    'eigvecs',
    'seigsys',
    'seigvals',
    'seigvecs',
    'groundstate',
    'groundenergy',
    'bound_spectrum',
    'eigsys_window',
    'eigvals_window',
    'eigvecs_window',
    'svd',
    'svds',
    'norm',
    # Gen ------------------------------------------------------------------- #
    'spin_operator',
    'sig',
    'controlled',
    'ham_heis',
    'ham_j1j2',
    'zspin_projector',
    'swap',
    'basis_vec',
    'up',
    'zplus',
    'down',
    'zminus',
    'plus',
    'xplus',
    'minus',
    'xminus',
    'yplus',
    'yminus',
    'bloch_state',
    'bell_state',
    'singlet',
    'thermal_state',
    'neel_state',
    'singlet_pairs',
    'werner_state',
    'ghz_state',
    'w_state',
    'levi_civita',
    'perm_state',
    'graph_state_1d',
    'rand_matrix',
    'rand_herm',
    'rand_pos',
    'rand_rho',
    'rand_ket',
    'rand_uni',
    'rand_haar_state',
    'gen_rand_haar_states',
    'rand_mix',
    'rand_product_state',
    'rand_matrix_product_state',
    'rand_mps',
    'rand_seperable',
    # Calc ------------------------------------------------------------------ #
    'expm',
    'sqrtm',
    'expm_multiply',
    'fidelity',
    'purify',
    'entropy',
    'entropy_subsys',
    'mutual_information',
    'mutinf',
    'mutinf_subsys',
    'partial_transpose',
    'negativity',
    'logarithmic_negativity',
    'logneg',
    'logneg_subsys',
    'concurrence',
    'one_way_classical_information',
    'quantum_discord',
    'trace_distance',
    'decomp',
    'pauli_decomp',
    'bell_decomp',
    'correlation',
    'pauli_correlations',
    'ent_cross_matrix',
    'qid',
    'is_degenerate',
    'is_eigenvector',
    'page_entropy',
    # Evo ------------------------------------------------------------------- #
    'QuEvo',
    # Approx spectral ------------------------------------------------------- #
    'approx_spectral_function',
    'tr_abs_approx',
    'tr_exp_approx',
    'tr_sqrt_approx',
    'tr_xlogx_approx',
    'entropy_subsys_approx',
    'logneg_subsys_approx',
    'negativity_subsys_approx',
]
