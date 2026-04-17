export function validateForm(name) {
  if (!name) return false;
  return name.length > 3;
}