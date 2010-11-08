# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcDC2A(ExcitationSystem):
    """IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.
    """

    def __init__(self, te=0.0, ke=0.0, e1=0.0, tc=0.0, se2=0.0, tb=0.0, uelin=0.0, e2=0.0, tf=0.0, kf=0.0, vrmax=0.0, se1=0.0, ta=0.0, ka=0.0, tr=0.0, exclim=0.0, vrmin=0.0, *args, **kw_args):
        """Initialises a new 'ExcDC2A' instance.

        @param te: Exciter time constant (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param tc: Lead time constant 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param tf: Rate feedback time constant, sec. (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param vrmax: Maximum controller output 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param ta: Time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param vrmin: Minimum controller output (&lt; 0.) 
        """
        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: Exciter field resistance line slope
        self.ke = ke

        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Lead time constant
        self.tc = tc

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        #: Lag time constant (&gt;= 0.)
        self.tb = tb

        #: UEL input: if &lt; 2, HV gate; if = 2, add to error signal
        self.uelin = uelin

        #: Field voltage value 2.    (&gt; 0.)
        self.e2 = e2

        #: Rate feedback time constant, sec. (&gt; 0.)
        self.tf = tf

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Maximum controller output
        self.vrmax = vrmax

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: If not 0, apply lower limit of 0. to exciter output
        self.exclim = exclim

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        super(ExcDC2A, self).__init__(*args, **kw_args)

    _attrs = ["te", "ke", "e1", "tc", "se2", "tb", "uelin", "e2", "tf", "kf", "vrmax", "se1", "ta", "ka", "tr", "exclim", "vrmin"]
    _attr_types = {"te": float, "ke": float, "e1": float, "tc": float, "se2": float, "tb": float, "uelin": float, "e2": float, "tf": float, "kf": float, "vrmax": float, "se1": float, "ta": float, "ka": float, "tr": float, "exclim": float, "vrmin": float}
    _defaults = {"te": 0.0, "ke": 0.0, "e1": 0.0, "tc": 0.0, "se2": 0.0, "tb": 0.0, "uelin": 0.0, "e2": 0.0, "tf": 0.0, "kf": 0.0, "vrmax": 0.0, "se1": 0.0, "ta": 0.0, "ka": 0.0, "tr": 0.0, "exclim": 0.0, "vrmin": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

