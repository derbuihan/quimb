import pytest

import quimb.tensor as qtn


class TestPEPSConstruct:

    @pytest.mark.parametrize('Lx', [3, 4, 5])
    @pytest.mark.parametrize('Ly', [3, 4, 5])
    def test_basic_rand(self, Lx, Ly):
        psi = qtn.PEPS.rand(Lx, Ly, bond_dim=4)

        assert psi.max_bond() == 4
        assert psi.Lx == Lx
        assert psi.Ly == Ly
        assert len(psi.tensor_map) == Lx * Ly
        assert psi.site_inds == tuple(
            f'k{i},{j}' for i in range(Lx) for j in range(Ly)
        )
        assert psi.site_tags == tuple(
            f'I{i},{j}' for i in range(Lx) for j in range(Ly)
        )

        assert psi.bond_size((1, 1), (1, 2)) == (4)

        for i in range(Lx):
            assert len(psi.select(f'ROW{i}').tensor_map) == Ly
        for j in range(Ly):
            assert len(psi.select(f'COL{j}').tensor_map) == Lx

        for i in range(Lx):
            for j in range(Ly):
                assert psi.phys_dim(i, j) == 2
                assert isinstance(psi[i, j], qtn.Tensor)
                assert isinstance(psi[f'I{i},{j}'], qtn.Tensor)

        if Lx == Ly == 3:
            psi_dense = psi.to_dense(optimize='random-greedy')
            assert psi_dense.shape == (512, 1)

        psi.show()
        assert f'Lx={Lx}' in psi.__str__()
        assert f'Lx={Lx}' in psi.__repr__()

    def test_flatten(self):
        psi = qtn.PEPS.rand(3, 5, 3, seed=42)
        norm = psi.H & psi
        assert len(norm.tensors) == 30
        norm.flatten_()
        assert len(norm.tensors) == 15
        assert norm.max_bond() == 9


class Test2DContract:

    def test_contract_2d_one_layer_boundary(self):
        psi = qtn.PEPS.rand(4, 4, 3, seed=42)
        norm = psi.H & psi
        xe = norm.contract(all, optimize='auto-hq')
        xt = norm.contract_boundary(max_bond=9)
        assert xt == pytest.approx(xe, rel=1e-2)

    def test_contract_2d_two_layer_boundary(self):
        psi = qtn.PEPS.rand(4, 4, 3, seed=42, tags='KET')
        norm = psi.retag({'KET': 'BRA'}).H | psi
        xe = norm.contract(all, optimize='auto-hq')
        xt = norm.contract_boundary(max_bond=27, layer_tags=['KET', 'BRA'])
        assert xt == pytest.approx(xe, rel=1e-2)

    @pytest.mark.parametrize("two_layer", [False, True])
    def test_compute_row_envs(self, two_layer):
        psi = qtn.PEPS.rand(5, 4, 2, seed=42, tags='KET')
        norm = psi.retag({'KET': 'BRA'}).H | psi
        ex = norm.contract(all)

        if two_layer:
            compress_opts = {'cutoff': 1e-6, 'max_bond': 12,
                             'layer_tags': ['KET', 'BRA']}
        else:
            compress_opts = {'cutoff': 1e-6, 'max_bond': 8}
        row_envs = norm.compute_row_environments(**compress_opts)

        for i in range(norm.Lx):
            norm_i = (
                row_envs['below', i] &
                norm.select(norm.row_tag(i)) &
                row_envs['above', i]
            )
            x = norm_i.contract(all)
            assert x == pytest.approx(ex, rel=1e-2)

    @pytest.mark.parametrize("two_layer", [False, True])
    def test_compute_col_envs(self, two_layer):
        psi = qtn.PEPS.rand(4, 5, 2, seed=42, tags='KET')
        norm = psi.retag({'KET': 'BRA'}).H | psi
        ex = norm.contract(all)

        if two_layer:
            compress_opts = {'cutoff': 1e-6, 'max_bond': 12,
                             'layer_tags': ['KET', 'BRA']}
        else:
            compress_opts = {'cutoff': 1e-6, 'max_bond': 8}
        col_envs = norm.compute_col_environments(**compress_opts)

        for j in range(norm.Lx):
            norm_j = (
                col_envs['left', j] &
                norm.select(norm.col_tag(j)) &
                col_envs['right', j]
            )
            x = norm_j.contract(all)
            assert x == pytest.approx(ex, rel=1e-2)
