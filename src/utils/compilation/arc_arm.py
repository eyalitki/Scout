from .target_arc import targetArc

class arcArm(targetArc):
    """A class representing an Arm CPU architecture to which we will compile our binary.

    Attributes
    ----------
        is_pic (bool): True iff a position-independent compilation
        is_32_bits (bool): True iff compiling a 32-bits binary

    Notes
    -----
        Can be extended by the Arm-Thumb architecture class.
    """

    # Arm Toolchain (32-bits)
    arm_compiler_path = '/usr/bin/arm-none-eabi-gcc'
    arm_linker_path   = '/usr/bin/arm-none-eabi-ld'
    arm_objcopy_path  = '/usr/bin/arm-none-eabi-objcopy'

    # Arm Toolchain (64-bits)
    aarch64_compiler_path = '/usr/bin/aarch64-linux-gnu-gcc'
    aarch64_linker_path   = '/usr/bin/aarch64-linux-gnu-ld'
    aarch64_objcopy_path  = '/usr/bin/aarch64-linux-gnu-objcopy'

    arm_objcopy_flags = ('--section-alignment 4',)

    arm_pic_32bits_compile_flags = ('mapcs-frame',)
    arm_pic_compile_flags = ('fno-jump-tables',)

    def __init__(self, is_pic):
        """Init the compilation configuration for the Arm architecture.

        Args:
            is_pic (bool): True iff a position-independent compilation
        """
        super(arcArm, self).__init__(is_pic)
        self.is_pic = is_pic
        # Arc specific PIC flags
        if is_pic:
            self.compile_flags += self.arm_pic_compile_flags

    @staticmethod
    def name():
        """Get the architecture's name.

        Return Value:
            String name for the architecture
        """
        return "Arm"

    # Overridden base function
    def setNotNative(self):
        """Mark the compilation as using a toolchain and not the native compiler."""
        if self.is_32_bits:
            self.setToolchain(self.arm_compiler_path, self.arm_linker_path, self.arm_objcopy_path, self.arm_objcopy_flags)
        else:
            self.setToolchain(self.aarch64_compiler_path, self.aarch64_linker_path, self.aarch64_objcopy_path, self.arm_objcopy_flags)

    # Overridden base function
    def setEndianness(self, is_little):
        """Set the (little/big) endianness we are going to use.

        Args:
            is_little (bool): True iff compiling a Little Endian binary
        """
        if is_little:
            self.compile_flags += ('mlittle-endian',)
            self.link_flags    += ('EL',)
        else:
            self.compile_flags += ('mbig-endian',)
            self.link_flags    += ('EB',)

    # Overridden base function
    def setBitness(self, is_32_bits):
        """Set the (32/64) bitness we are going to use.

        Args:
            is_32_bits (bool): True iff compiling a 32-bits binary
        """
        self.is_32_bits = is_32_bits
        if not is_32_bits or not self.is_pic:
            return
        self.compile_flags += arm_pic_32bits_compile_flags

class arcArmThumb(arcArm):
    """A class representing an Arm CPU architecture to which we will compile our Thumb binary.

    Attributes
    ----------
        (all inherited from the base class)
    """

    def __init__(self, is_pic):
        """Init the compilation configuration for the Arm-Thumb architecture.

        Args:
            is_pic (bool): True iff a position-independent compilation
        """
        super(arcArmThumb, self).__init__(is_pic)
        # Arc specific flags
        self.compile_flags += ('mthumb',)

    @staticmethod
    def name():
        """Get the architecture's name.

        Return Value:
            String name for the architecture
        """
        return "Arm-Thumb"

    # Overridden base function
    def setBitness(self, is_32_bits):
        """Set the (32/64) bitness we are going to use.

        Args:
            is_32_bits (bool): True iff compiling a 32-bits binary
        """
        if not is_32_bits:
            raise Exception("ARM-Thumb is not supported over a 64 bits architecture")
