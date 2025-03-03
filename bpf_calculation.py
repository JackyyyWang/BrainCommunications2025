import nibabel as nib
import numpy as np

def calculate_bpf(segmentation_path):
    """
    Calculates the Brain Parenchyma Fraction (BPF) from a segmentation map.
    
    Args:
        segmentation_path (str): Path to the NIfTI segmentation file (.nii or .nii.gz).
    
    Returns:
        float: Brain Parenchyma Fraction (BPF) value.
    """
    # Load the segmentation map
    seg_img = nib.load(segmentation_path)
    seg_data = seg_img.get_fdata()
    
    # Compute volume of each tissue type
    wm_volume = np.sum(seg_data == 1)  # White matter
    gm_volume = np.sum(seg_data == 2)  # Gray matter
    csf_volume = np.sum(seg_data == 3)  # Cerebrospinal fluid
    
    # Calculate BPF
    total_brain_volume = wm_volume + gm_volume + csf_volume
    if total_brain_volume == 0:
        raise ValueError("Segmentation map contains no valid brain tissues.")
    
    bpf = (wm_volume + gm_volume) / total_brain_volume
    
    return bpf

# Example usage
segmentation_file = "path/to/segmentation.nii.gz"  # Update with the actual file path
bpf_value = calculate_bpf(segmentation_file)
print(f"Brain Parenchyma Fraction (BPF): {bpf_value:.4f}")
